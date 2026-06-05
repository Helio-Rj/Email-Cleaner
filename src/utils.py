import json


def carregar_config():
    """Carrega a configuração armazenada no arquivo JSON.

    O arquivo `config/settings.json` contém a lista de remetentes que devem
    ser removidos da caixa de entrada.
    """

    # Abre o arquivo de configuração para leitura.
    with open(
        "config/settings.json",
        "r",
        encoding="utf-8"
    ) as arquivo:

        # Converte o conteúdo JSON num dicionário Python.
        return json.load(arquivo)
