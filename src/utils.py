import os


def carregar_config():
    """
    Carrega as credenciais do Gmail a partir das variáveis de ambiente
    definidas nos GitHub Secrets.
    """
    return {
        "client_id": os.environ.get("GMAIL_CLIENT_ID"),
        "client_secret": os.environ.get("GMAIL_CLIENT_SECRET"),
        "refresh_token": os.environ.get("GMAIL_REFRESH_TOKEN")
    }
