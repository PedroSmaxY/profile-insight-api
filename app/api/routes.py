from http import HTTPStatus
from fastapi import APIRouter, HTTPException
from typing import List

from ..schemas.perfil_answer import PerfilAnswer
from ..services.prolog_service import PrologService


routes = APIRouter()

prolog_service = PrologService()


@routes.get("/questions/{perfil}/{num}/")
async def get_question(perfil: str, num: int):
    question: str = prolog_service.get_question(perfil, num)

    if question is None:
        raise HTTPException(HTTPStatus.NOT_FOUND, "Question not found")

    return { "question": question }


@routes.post("/diagnostic/")
async def score_calc(perfil: str, answers: List[int]):
    diagnostic: str = prolog_service.score_calc(perfil, answers)

    if diagnostic is None:
        raise HTTPException(HTTPStatus.BAD_REQUEST, "Invalid data or no result")

    return {"diagnostic": diagnostic}


@routes.post("/diagnostic/complete/")
async def complete_score_calc(answer: PerfilAnswer):
    answer_dict = answer.model_dump()
    results = {}

    for perfil, answers_perfil in answer_dict.items():
        result = prolog_service.score_calc(perfil, answers_perfil)
        results[perfil] = result

    return results
