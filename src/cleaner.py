def apagar_remetente(service, email):
    apagados = 0
    page_token = None

    while True:
        resultado = service.users().messages().list(
            userId="me",
            q=f"from:{email}",
            pageToken=page_token
        ).execute()

        mensagens = resultado.get("messages", [])

        if not mensagens:
            break

        for msg in mensagens:
            service.users().messages().trash(
                userId="me",
                id=msg["id"]
            ).execute()

            apagados += 1

        page_token = resultado.get("nextPageToken")

        if not page_token:
            break

    return apagados
