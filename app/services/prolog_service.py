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

    def score_calc(self, perfil: str, answer: list[int]):
        answer_str = ', '.join(map(str, answer))
        consult = f"diagnostico({perfil}, [{answer_str}], Diagnostico)"

        for result in self.prolog.query(consult):
            return result['Diagnostico']
        return None
