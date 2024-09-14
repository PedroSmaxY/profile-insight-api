from pyswip import Prolog
import os

PROLOG_FILE_PATH = os.path.abspath("../prolog/knowledge.prolog")


class PrologService:
    def __init__(self):
        self.prolog = Prolog()

    def get_question(self, perfil: str, num: int):
        self.prolog.consult(PROLOG_FILE_PATH)

        consult = f"pergunta({perfil}, {num}, Pergunta)"
        for result in self.prolog.query(consult):
            return result['Pergunta']


if __name__ == "__main__":
    prolog = Prolog()
    prolog.consult(PROLOG_FILE_PATH)

    def obter_pergunta(perfis, num):
        consulta = f"pergunta({perfis}, {num}, Pergunta)"
        for resultado in prolog.query(consulta):
            return resultado['Pergunta']

    def calcular_pontuacao(respostas):
        respostas_str = ', '.join(map(str, respostas))
        consulta = f"calcular_pontuacao([{respostas_str}], Total)"
        for resultado in prolog.query(consulta):
            return resultado['Total']

    perfis = ['influencia', 'dominancia', 'conformidade','estabilidade']
    respostas = []


    for num in range(1, 6):
        for perfil in perfis:
            pergunta = obter_pergunta(perfil, num)
            print(f"Pergunta {num}: {pergunta}")
            resposta = int(input(f"Responda (1 a 5) para a pergunta {num}: "))
            respostas.append(resposta)
            print("\n" * 50)


    pontuacao_total = calcular_pontuacao(respostas)
    print(f"Pontuação total para {perfis}: {pontuacao_total}")