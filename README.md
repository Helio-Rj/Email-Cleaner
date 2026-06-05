# Autoria: Helio Rj — GitHub: [@Helio-Rj](https://github.com/Helio-Rj)



# Email-Cleaner

Um utilitário Python simples para limpar automaticamente emails indesejados no Gmail com base em uma lista negra de remetentes.

## 🚀 Visão geral

O `Email-Cleaner` conecta-se à API do Gmail usando OAuth 2.0, pesquisa mensagens por remetente e move esses emails para a lixeira. Ideal para manter sua caixa de entrada organizada removendo newsletters, alertas automáticos e mensagens de remetentes não desejados.

## ✅ Funcionalidades

- Autenticação segura usando OAuth do Google
- Busca por emails de remetentes listados em `config/settings.json`
- Exclusão em massa de mensagens encontradas
- Contagem total de emails removidos

## 📁 Estrutura do projeto

- `src/main.py` — ponto de entrada da aplicação
- `src/auth.py` — autenticação com Gmail via Google OAuth
- `src/cleaner.py` — lógica de pesquisa e exclusão de emails
- `src/utils.py` — carregamento de configuração
- `config/settings.json` — lista de emails a serem removidos
- `credentials.json` — credenciais de cliente OAuth (arquivo privado)

gmail-cleaner/
│
├── credentials.json
│
├── config/
│   └── settings.json
│
└── src/
    ├── main.py
    ├── auth.py
    ├── cleaner.py
    └── utils.py

## 🛠️ Requisitos

- Python 3.9+
- Biblioteca `google-auth-oauthlib`
- Biblioteca `google-api-python-client`

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/Email-Cleaner.git
cd Email-Cleaner
```

2. Instale as dependências:

```bash
pip install google-auth-oauthlib google-api-python-client
```

3. Crie ou atualize o arquivo `credentials.json` com as credenciais do Google Cloud Console.

4. Edite `config/settings.json` para incluir os remetentes que você deseja apagar.

## ▶️ Uso

Execute o script principal:

```bash
python src/main.py
```

A aplicação abrirá o navegador para autenticar sua conta Google e em seguida começará a buscar e mover para a lixeira os emails dos remetentes da lista negra.

## ⚠️ Observações importantes

- O script usa o escopo `https://www.googleapis.com/auth/gmail.modify`, que permite modificar mensagens na sua conta.
- Nunca faça commit de credenciais reais no GitHub. Use `credentials.json` apenas localmente ou adicione-o ao `.gitignore`.
- O processo move mensagens para a lixeira, em vez de excluí-las permanentemente.

## 🔧 Configuração da lista negra

Edite `config/settings.json` para adicionar ou remover remetentes:

```json
{
  "lista_negra": [
    "spam@example.com",
    "news@newsletter.com"
  ]
}
```

## 💡 Sugestões de melhoria

- Adicionar suporte a exclusão de emails por assunto ou data
- Implementar um modo de simulação (`dry-run`)
- Gerar um relatório de emails apagados
- Incluir testes automatizados

## 📜 Licença

Este projeto é fornecido como exemplo e pode ser usado livremente para fins pessoais ou educacionais.
"  
