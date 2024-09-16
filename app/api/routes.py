from http import HTTPStatus

from fastapi import APIRouter, HTTPException, Depends
from ..services.prolog_service import PrologService

routes = APIRouter()

prolog_service = PrologService()

@routes.get("/questions/{perfil}/{num}")
async def get_questions(perfil: str, num: int):
    question: str = prolog_service.get_question(perfil, num)

    if question is None:
        raise HTTPException(HTTPStatus.NOT_FOUND, "Question not found")

    return { "question": question }