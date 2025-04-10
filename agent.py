import os
from dotenv import load_dotenv

from langchain.utilities import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.chat_models import ChatOpenAI
from crewai import Agent

load_dotenv()
db_uri = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@" \
         f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Conecta ao banco
db = SQLDatabase.from_uri(db_uri)

# Cria o LLM
llm = ChatOpenAI(temperature=0)

# Cria as tools com base no banco
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools = toolkit.get_tools()

# Agente Pesquisador - Coleta dados do banco
pesquisador = Agent(
    role='Pesquisador Técnico',
    goal='Coletar informações atualizadas sobre IA Generativa e dados do banco',
    backstory='Expert em pesquisa com foco em inovação e tecnologia. Tem acesso a um banco de dados.',
    tools=tools,
    verbose=True
)

# Agente Redator - Usa dados coletados para escrever o conteúdo
redator = Agent(
    role='Redator de Conteúdo',
    goal='Escrever artigos com clareza e boa estrutura usando os dados coletados',
    backstory='Formado em jornalismo, especialista em tecnologia.',
    verbose=True
)

# Agente Revisor - Revisa o conteúdo escrito pelo Redator
revisor = Agent(
    role='Revisor de Texto',
    goal='Revisar ortografia, gramática e coesão textual',
    backstory='Editor experiente, atento a detalhes.',
    verbose=True
)

# Simulando o fluxo de trabalho
def fluxo_trabalho():
    
    # Pesquisador coleta os dados
    dados_coletados = pesquisador.act("Coletar informações sobre IA Generativa e dados do banco.")
    
    # Redator usa os dados coletados para escrever um conteúdo
    artigo_escrito = redator.act(f"Usando os dados coletados: {dados_coletados}. Escrever um artigo sobre IA Generativa.")
    
    # Revisor revisa o conteúdo escrito
    artigo_revisado = revisor.act(f"Revisar o seguinte artigo: {artigo_escrito}")
    
    return artigo_revisado


artigo_final = fluxo_trabalho()
print(artigo_final)
