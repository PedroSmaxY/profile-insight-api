from pyswip import Prolog
import os
import platform

prolog = Prolog()

prolog.consult("../prolog/knowledge.prolog")


def name():
    return "name"



if __name__ == "__main__":

    def obter_pergunta(perfis, num):
        """Consulta Prolog para obter uma pergunta com base no perfil e número"""
        consulta = f"pergunta({perfis}, {num}, Pergunta)"
        for resultado in prolog.query(consulta):
            return resultado['Pergunta']

    def calcular_pontuacao(respostas):
        """Calcula a pontuação total das respostas"""
        respostas_str = ', '.join(map(str, respostas))  # Converte a lista de respostas em uma string
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


            # Calculando a pontuação total
    pontuacao_total = calcular_pontuacao(respostas)
    print(f"Pontuação total para {perfis}: {pontuacao_total}")