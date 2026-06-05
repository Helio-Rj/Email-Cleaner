import json


def carregar_config():
    """Carrega a configuração armazenada no arquivo JSON.

    O arquivo `config/settings.json` contém a lista de remetentes que devem
    ser removidos da caixa de entrada.
    """
    with open("../config/settings.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def mostrar_resultado(remetente, quantidade):
    """Exibe o resultado da exclusão de mensagens para um remetente."""
    if quantidade > 0:
        print(f"Remetente: {remetente} → {quantidade} mensagens apagadas")
    else:
        print(f"Remetente: {remetente} → nenhuma mensagem encontrada")
