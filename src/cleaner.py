def apagar_remetente(service, email, limite_global, contador_global):
    """Apaga (move para a lixeira) todas as mensagens de um remetente.

    Args:
        service: Objeto de serviço autenticado da API Gmail.
        email: Endereço de email do remetente a ser removido.
        limite_global: número máximo de mensagens a apagar no total.
        contador_global: contador atual de mensagens apagadas.

    Retorna:
        O total de mensagens removidas para esse remetente
        e o contador global atualizado.
    """
    apagados = 0
    page_token = None

    print(f"\n🔎 Iniciando busca por mensagens de {email}...")

    while True:
        # Se já atingiu o limite global, interrompe
        if contador_global >= limite_global:
            print(f"⛔ Limite global de {limite_global} atingido. Encerrando busca.")
            break

        resultado = service.users().messages().list(
            userId="me",
            q=f"from:{email}",
            pageToken=page_token
        ).execute()

        mensagens = resultado.get("messages", [])
        if not mensagens:
            break

        for msg in mensagens:
            if contador_global >= limite_global:
                print(f"⛔ Limite global de {limite_global} atingido. Parando em {email}.")
                break

            try:
                service.users().messages().trash(
                    userId="me",
                    id=msg["id"]
                ).execute()
                apagados += 1
                contador_global += 1
                print(f"🗑️ Apagada mensagem {msg['id']} de {email} "
                      f"(total {apagados} desse remetente, {contador_global} no geral)")
            except Exception as e:
                print(f"⚠️ Erro ao apagar mensagem {msg['id']} de {email}: {e}")

        page_token = resultado.get("nextPageToken")
        if not page_token or contador_global >= limite_global:
            break

    print(f"✅ Concluído para {email}: {apagados} mensagens apagadas.\n")
    return apagados, contador_global
