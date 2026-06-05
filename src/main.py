from auth import autenticar_gmail
from cleaner import apagar_remetente
from utils import carregar_config


def main():
    """Função principal do programa.

    Carrega a lista de remetentes a serem removidos, autentica no Gmail
    e chama a função de limpeza para cada remetente.
    """

    # Carrega as configurações do arquivo JSON.
    config = carregar_config()
    lista_negra = config["lista_negra"]

    # Cria um serviço autenticado da API Gmail.
    service = autenticar_gmail()

    total_apagados = 0

    # Para cada remetente da lista negra, busca e apaga mensagens.
    for remetente in lista_negra:
        print(f"\nProcurando: {remetente}")

        quantidade = apagar_remetente(
            service,
            remetente
        )

        print(f"Apagados: {quantidade}")

        total_apagados += quantidade

    # Exibe o total de mensagens removidas no final.
    print("\n======================")
    print(f"TOTAL APAGADO: {total_apagados}")
    print("======================")


if __name__ == "__main__":
    # Garante que a função main seja executada apenas quando o ‘script’ for chamado diretamente.
    main()
