from pyswip import Prolog


PROLOG_FILE_PATH = "./app/prolog/knowledge.prolog"


class PrologService:
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult(PROLOG_FILE_PATH)

    def _execute_query(self, consult: str, var_name: str):
        result = next(self.prolog.query(consult), None)
        return result.get(var_name) if result else None

    def get_question(self, perfil: str, num: int) -> str | None:
        consult = f"pergunta({perfil}, {num}, Pergunta)"
        return self._execute_query(consult, 'Pergunta')

    def score_calc(self, perfil: str, answers: list[int]) -> str | None:
        answers_str = ', '.join(map(str, answers))
        consult = f"diagnostico({perfil}, [{answers_str}], Diagnostico)"
        return self._execute_query(consult, 'Diagnostico')
