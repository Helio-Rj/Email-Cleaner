from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Escopos de acesso necessários para modificar mensagens no Gmail.
# O escopo `gmail.modify` permite ler, enviar, excluir e arquivar mensagens.
SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify"
]


def autenticar_gmail():
    """Autentica o usuário no Google e retorna um serviço da API Gmail.

    A função usa o arquivo `credentials.json` para iniciar o fluxo OAuth
    e abre um servidor local para completar a autenticação no navegador.
    """

    # Cria um fluxo de autenticação usando as credenciais do cliente.
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json",
        SCOPES
    )

    # Executa o fluxo local para o usuário autorizar o acesso.
    creds = flow.run_local_server(port=0)

    # Constrói o serviço da API Gmail com as credenciais autenticadas.
    return build(
        "gmail",
        "v1",
        credentials=creds
    )
