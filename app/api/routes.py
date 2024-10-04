from http import HTTPStatus
from fastapi import APIRouter, HTTPException
from typing import List, Dict
from ..schemas.perfil_answers import PerfilAnswers
from ..services.prolog_service import PrologService


routes = APIRouter()
prolog_service = PrologService()


@routes.get("/questions/{perfil}/{num}/", response_model=Dict[str, str])
async def get_question(perfil: str, num: int):
    question: str = prolog_service.get_question(perfil, num)

    if question is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Question not found")

    return {"question": question}


@routes.post("/diagnostic/", response_model=Dict[str, str])
async def score_calc(perfil: str, answers: List[int]):
    diagnostic: str = prolog_service.score_calc(perfil, answers)

    if diagnostic is None:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Invalid data or no result")

    return {"diagnostic": diagnostic}


@routes.post("/diagnostic/complete/", response_model=Dict[str, str])
async def complete_score_calc(answers: PerfilAnswers):
    answers_dict = answers.model_dump()

    results = {}

    for perfil, answers_perfil in answers_dict.items():
        result = prolog_service.score_calc(perfil, answers_perfil)

        if result is None:
            raise HTTPException(HTTPStatus.BAD_REQUEST, "Invalid data or no result for one or more profiles")

        results[perfil] = result

    return results
