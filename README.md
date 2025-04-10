#Projeto de Agentes Colaborativos para Criação de Artigos
Este projeto utiliza a framework CrewAI juntamente com o LangChain para criar uma rede de agentes colaborativos que coletam informações, redigem e revisam artigos sobre IA Generativa, utilizando dados extraídos de um banco de dados PostgreSQL.

##🛠️ Tecnologias Utilizadas
Python (versão 3.8 ou superior)

CrewAI - Framework para criação de agentes inteligentes colaborativos

LangChain - Framework para integrar ferramentas de LLMs (Modelos de Linguagem) com agentes

PostgreSQL - Banco de dados relacional utilizado para armazenar e consultar dados

dotenv - Para carregar variáveis de ambiente do arquivo .env

OpenAI (ChatGPT) - Modelo de linguagem para os agentes

##⚙️ Configuração
###1. Instalar dependências
Crie um ambiente virtual no seu projeto e instale as dependências necessárias:

bash
Copiar
Editar
### Criar ambiente virtual
python -m venv venv

### Ativar o ambiente virtual
### No Windows
venv\Scripts\activate
### No Mac/Linux
source venv/bin/activate

### Instalar as dependências
pip install -r requirements.txt
O arquivo requirements.txt deve conter:

nginx
Copiar
Editar
crewai
langchain
openai
psycopg2
python-dotenv
##2. Configurar as variáveis de ambiente
Crie um arquivo .env na raiz do projeto com as seguintes variáveis:

ini
Copiar
Editar
DB_USER=seu_usuario
DB_PASS=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
OPENAI_API_KEY=chave_da_api_do_openai
Certifique-se de substituir os valores pelos detalhes do seu banco de dados e sua chave da API do OpenAI.

##3. Banco de Dados
Este projeto utiliza PostgreSQL como banco de dados. As consultas e interações com o banco de dados são realizadas através do LangChain, que conecta-se ao banco e extrai informações relevantes para o artigo.

Você pode usar um banco de dados local ou configurar um banco remoto. Certifique-se de que a conexão com o banco de dados esteja configurada corretamente no arquivo .env.

##4. Executando o Projeto
Para rodar o projeto, execute o seguinte comando:

bash
Copiar
Editar
python main.py
Este comando executa o fluxo de trabalho onde os agentes colaboram para criar um artigo. O Pesquisador coleta dados do banco de dados, o Redator escreve o artigo utilizando esses dados e o Revisor revisa o conteúdo gerado.

##📂 Estrutura do Projeto
bash
Copiar
Editar
meu_projeto/
│
├── agents.py          # Define os agentes colaborativos (Pesquisador, Redator, Revisor)
├── crew.py            # Lógica de integração entre os agentes
├── main.py            # Arquivo principal que orquestra o fluxo de trabalho
├── tasks.py           # Define as tarefas e funções específicas dos agentes
├── requirements.txt   # Dependências do projeto
├── .env               # Arquivo de variáveis de ambiente
└── venv/              # Ambiente virtual (gerado automaticamente)
##💡 Como Funciona?
Pesquisador Técnico: Este agente é responsável por coletar informações sobre IA Generativa e dados atualizados do banco de dados. Ele utiliza ferramentas como queries SQL para extrair dados.

Redator de Conteúdo: O agente redator utiliza os dados coletados pelo Pesquisador para criar um artigo claro e bem estruturado sobre IA Generativa.

Revisor de Texto: Este agente revisa o conteúdo gerado pelo Redator, verificando ortografia, gramática e coesão textual.

A interação entre os agentes ocorre dentro dos arquivos agents.py e crew.py, onde o fluxo de trabalho é orquestrado de forma sequencial. O Pesquisador começa o processo coletando os dados, o Redator utiliza esses dados para criar o conteúdo e o Revisor verifica e ajusta o texto.

##🌱 Contribuindo
Contribuições são bem-vindas! Caso queira contribuir com o projeto, basta fazer um fork, realizar suas modificações e abrir um pull request.

Passos para Contribuir:
Faça um fork deste repositório.

Crie uma branch com sua nova funcionalidade (git checkout -b nova-funcionalidade).

Faça commit das suas alterações (git commit -m 'Adiciona nova funcionalidade').

Push para a sua branch (git push origin nova-funcionalidade).

Abra um pull request.

##🔑 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
