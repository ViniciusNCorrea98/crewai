from crewai import Task
from agents import pesquisador, redator, revisor

tarefa_pesquisa = Task(
    description='Pesquise os avanços mais recentes em IA Generativa em 2024.',
    expected_output='Resumo técnico com no mínimo 5 tópicos atualizados.',
    agent=pesquisador
)

tarefa_redacao = Task(
    description='Baseando-se na pesquisa, redija um artigo introdutório sobre IA Generativa para leigos.',
    expected_output='Artigo bem estruturado com introdução, desenvolvimento e conclusão.',
    agent=redator,
    async_execution=False,
    context=[tarefa_pesquisa]  # depende do output da tarefa anterior - 01
)

tarefa_revisao = Task(
    description='Revise o artigo, corrija erros e melhore a fluidez.',
    expected_output='Versão revisada e pronta para publicação.',
    agent=revisor,
    async_execution=False,
    context=[tarefa_redacao] # depende do output da tarefa anterior - 02
)
