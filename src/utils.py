import json


def carregar_config():
    """
    Lê e retorna o dicionário de configurações do arquivo `config/settings.json`.

    Formato esperado (exemplo):
    {
        "lista_negra": [
            "spam@exemplo.com",
            "newsletter@exemplo.com"
        ]
    }

    Observações:
    - O caminho usado é relativo ao diretório `src/` atual: `../config/settings.json`.
      Se executar o script a partir de outro diretório, ajuste o caminho.
    - Em projetos maiores, prefira caminhos absolutos ou variáveis de ambiente
      para localizar arquivos de configuração.
    """
    with open("../config/settings.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def mostrar_resultado(remetente, quantidade):
    """
    Função utilitária para exibir no console quantas mensagens foram
    apagadas para um determinado remetente.

    Parâmetros:
        remetente: string com o endereço do remetente
        quantidade: inteiro com a quantidade de mensagens removidas
    """
    if quantidade > 0:
        print(f"Remetente: {remetente} → {quantidade} mensagens apagadas")
    else:
        print(f"Remetente: {remetente} → nenhuma mensagem encontrada")
