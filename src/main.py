from auth import autenticar_gmail
from cleaner import apagar_remetente
from utils import carregar_config


def main():
    config = carregar_config()
    lista_negra = config["lista_negra"]

    service = autenticar_gmail()

    total_apagados = 0
    limite_global = 3000

    print("\n🚀 Iniciando limpeza de e-mails...\n")

    for remetente in lista_negra:
        apagados, total_apagados = apagar_remetente(service, remetente, limite_global, total_apagados)
        if total_apagados >= limite_global:
            print("\n⛔ Limite global atingido. Encerrando execução.")
            break

    print("\n==================================================")
    print("✅ LIMPEZA CONCLUÍDA")
    print(f"📊 TOTAL DE MENSAGENS APAGADAS: {total_apagados} (limite {limite_global})")
    print("==================================================")


if __name__ == "__main__":
    main()
