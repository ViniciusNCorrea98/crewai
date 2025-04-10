from crewai import Crew
from agents import pesquisador, redator, revisor
from tasks import tarefa_pesquisa, tarefa_redacao, tarefa_revisao

tripulacao = Crew(
    agents=[pesquisador, redator, revisor],
    tasks=[tarefa_pesquisa, tarefa_redacao, tarefa_revisao],
    verbose=True
)
