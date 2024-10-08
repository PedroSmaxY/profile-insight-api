from typing import List
from pydantic import BaseModel


class PerfilAnswers(BaseModel):
    dominancia: List[int]
    influencia: List[int]
    estabilidade: List[int]
    conformidade: List[int]
