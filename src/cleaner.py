def apagar_remetente(service, email, limite_global, contador_global):
    """
    Percorre e remove (move para a lixeira) mensagens de um remetente específico.

    Detalhes de funcionamento:
    - Usa a API `users().messages().list()` para buscar mensagens filtradas por
      remetente (`q="from:<email>"`). A API retorna os IDs das mensagens.
    - Para cada mensagem encontrada, chama `users().messages().trash()` para
      movê-la para a lixeira (não a exclui permanentemente).
    - A busca usa paginação (campo `nextPageToken`) para percorrer todas as
      mensagens do remetente sem carregar tudo de uma vez.
    - O parâmetro `limite_global` é usado para limitar o total de mensagens
      apagadas durante toda a execução (útil para testar ou evitar ações massivas).

    Args:
        service: cliente autenticado da API Gmail (retorno de `build(...)`).
        email: endereço do remetente cujas mensagens serão processadas.
        limite_global: limite máximo de mensagens a apagar em toda a execução.
        contador_global: contador corrente de mensagens já apagadas (acumulado).

    Returns:
        (apagados, contador_global): `apagados` é o total removido para esse
        remetente; `contador_global` é o contador global atualizado.
    """
    apagados = 0
    page_token = None

    print(f"\n🔎 Iniciando busca por mensagens de {email}...")

    while True:
        # Interrompe se já alcançou o limite global
        if contador_global >= limite_global:
            print(f"⛔ Limite global de {limite_global} atingido. Encerrando busca.")
            break

        # Solicita uma página de resultados — a query pode retornar muitos IDs
        resultado = service.users().messages().list(
            userId="me",
            q=f"from:{email}",
            pageToken=page_token
        ).execute()

        # A API devolve uma lista de objetos com chave 'id'. Se vazia, encerra.
        mensagens = resultado.get("messages", [])
        if not mensagens:
            break

        for msg in mensagens:
            # Verifica novamente o limite antes de cada operação
            if contador_global >= limite_global:
                print(f"⛔ Limite global de {limite_global} atingido. Parando em {email}.")
                break

            try:
                # Move a mensagem para a lixeira usando seu ID
                service.users().messages().trash(
                    userId="me",
                    id=msg["id"]
                ).execute()

                apagados += 1
                contador_global += 1

                # Em contextos reais, considere armazenar logs em arquivo/serviço
                print(
                    f"🗑️ Apagada mensagem {msg['id']} de {email} "
                    f"(total {apagados} desse remetente, {contador_global} no geral)"
                )
            except Exception as e:
                # Erro na exclusão de uma mensagem não interrompe o processo
                print(f"⚠️ Erro ao apagar mensagem {msg['id']} de {email}: {e}")

        # Atualiza token de paginação; se inexistente, terminamos a iteração
        page_token = resultado.get("nextPageToken")
        if not page_token or contador_global >= limite_global:
            break

    print(f"✅ Concluído para {email}: {apagados} mensagens apagadas.\n")
    return apagados, contador_global
