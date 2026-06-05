def apagar_remetente(service, email):
    """Apaga (move para a lixeira) todas as mensagens de um remetente.

    Args:
        service: Objeto de serviço autenticado da API Gmail.
        email: Endereço de email do remetente a ser removido.

    Retorna:
        O total de mensagens removidas para esse remetente.
    """

    apagados = 0
    page_token = None

    # Loop para percorrer todas as páginas de resultados.
    while True:
        resultado = service.users().messages().list(
            userId="me",  # Usa a conta autenticada do usuário atual.
            q=f"from:{email}",  # Pesquisa apenas mensagens daquele remetente.
            pageToken=page_token
        ).execute()

        # Extrai a lista de mensagens retornadas, se houver.
        mensagens = resultado.get("messages", [])

        # Se não houver mensagens, encerra a busca.
        if not mensagens:
            break

        # Para cada mensagem encontrada, envia para a lixeira.
        for msg in mensagens:
            service.users().messages().trash(
                userId="me",
                id=msg["id"]
            ).execute()

            apagados += 1

        # Atualiza o ‘token’ da próxima página, caso existam mais resultados.
        page_token = resultado.get("nextPageToken")

        # Se não houver mais páginas, encerra o ‘loop’.
        if not page_token:
            break

    return apagados
