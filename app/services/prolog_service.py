from pyswip import Prolog

PROLOG_FILE_PATH = "./app/prolog/knowledge.prolog"

class PrologService:
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult(PROLOG_FILE_PATH)

    def get_question(self, perfil: str, num: int):
        consult = f"pergunta({perfil}, {num}, Pergunta)"
        for result in self.prolog.query(consult):
            return result['Pergunta']
        return None

    def calcular_pontuacao(self, answer):
        answers_str = ', '.join(map(str, answer))
        consult = f"calcular_pontuacao([{answers_str}], Total)"
        for result in self.prolog.query(consult):
            return result['Total']
        return None