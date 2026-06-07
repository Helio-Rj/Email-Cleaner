import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Escopos necessários para modificar (mover para lixeira) mensagens do Gmail.
# Usar apenas os escopos estritamente necessários é uma boa prática de segurança.
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]


def autenticar_gmail():
    """
    Autentica e retorna um cliente da API Gmail pronto para uso.

    Fluxo de autenticação:
    1. Tenta carregar credenciais previamente salvas em `token.json`.
    2. Se as credenciais não existem, estão expiradas sem refresh token,
       inicia o fluxo de autorização local (navegador) usando `credentials.json`.
    3. Se as credenciais expiraram mas possuem `refresh_token`, realiza
       o refresh de forma silenciosa.
    4. Salva o token atualizado em `token.json` para execuções futuras.

    Retorna:
        um objeto de serviço da Google API para interagir com o Gmail
        (equivalente ao retorno de `build("gmail", "v1", credentials=creds)`).

    Observações:
    - Este método depende de `credentials.json` (credenciais OAuth do projeto)
      e cria/atualiza `token.json` no diretório atual.
    - Em ambientes de produção ou CI, prefira armazenar tokens em local
      seguro (ex.: secret manager) em vez de arquivos locais.
    """
    creds = None

    # Carrega token salvo se existir — evita reautenticação manual a cada execução
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # Se não existe credencial válida, executa o fluxo de autenticação/refresh
    if not creds or not creds.valid:
        # Se existe e está expirado, mas tem refresh token, usa-o para renovar
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Abre um servidor local e guia o usuário pelo login OAuth no navegador
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Persiste o token atualizado para usos futuros
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Constroi e retorna o cliente de serviço da API Gmail
    return build("gmail", "v1", credentials=creds)
