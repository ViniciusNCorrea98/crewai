from crew import tripulacao
from dotenv import load_dotenv
load_dotenv()


if __name__ == "__main__":
    resultado_final = tripulacao.kickoff()
    print("\n🔍 Resultado Final:\n")
    print(resultado_final)
