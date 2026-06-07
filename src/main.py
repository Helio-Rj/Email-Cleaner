from auth import autenticar_gmail
from cleaner import apagar_remetente
from utils import carregar_config


def main():
    """
    Ponto de entrada do ‘script’.

    Fluxo principal:
    1. Carrega configuração (lista de remetentes) a partir de `config/settings.json`.
    2. Autentica no Gmail e obtém o cliente `service`.
    3. Itera sobre cada remetente da lista negra e chama `apagar_remetente`.
    4. Observa um `limite_global` para evitar remoções em massa não intencionais.
    """
    # Carrega configurações (espera chave `lista_negra` no JSON)
    config = carregar_config()
    lista_negra = config["lista_negra"]

    # Cliente autenticado para chamar a API Gmail
    service = autenticar_gmail()

    # Contadores e limites — ajustar conforme necessidade
    total_apagados = 0
    limite_global = 3000

    print("\n🚀 Iniciando limpeza de e-mails...\n")

    # Percorre cada remetente listado e solicita remoção da suas mensagens
    for remetente in lista_negra:
        apagados, total_apagados = apagar_remetente(
            service, remetente, limite_global, total_apagados
        )
        # Se o limite global foi atingido, interrompe o processo
        if total_apagados >= limite_global:
            print("\n⛔ Limite global atingido. Encerrando execução.")
            break

    # Resumo final — em produção, prefira gravar em ‘log’ estruturado
    print("\n==================================================")
    print("✅ LIMPEZA CONCLUÍDA")
    print(f"📊 TOTAL DE MENSAGENS APAGADAS: {total_apagados} (limite {limite_global})")
    print("==================================================")


if __name__ == "__main__":
    main()
