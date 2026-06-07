import os
import json


def carregar_config():
    # Credenciais sensíveis vindas dos Secrets
    config = {
        "client_id": os.environ["GMAIL_CLIENT_ID"],
        "client_secret": os.environ["GMAIL_CLIENT_SECRET"],
        "refresh_token": os.environ["GMAIL_REFRESH_TOKEN"]
    }

    # Configurações gerais vindas de arquivo versionado
    try:
        with open("config/appsettings.json", "r", encoding="utf-8") as f:
            extras = json.load(f)
            config.update(extras)
    except FileNotFoundError:
        print("⚠️ Arquivo de configuração não encontrado, usando apenas Secrets.")

    return config
