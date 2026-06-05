from auth import autenticar_gmail
from cleaner import apagar_remetente
from utils import carregar_config


def main():

    config = carregar_config()
    lista_negra = config["lista_negra"]

    service = autenticar_gmail()

    total_apagados = 0

    for remetente in lista_negra:

        print(f"\nProcurando: {remetente}")

        quantidade = apagar_remetente(
            service,
            remetente
        )

        print(f"Apagados: {quantidade}")

        total_apagados += quantidade

    print("\n======================")
    print(f"TOTAL APAGADO: {total_apagados}")
    print("======================")


if __name__ == "__main__":
    main()
