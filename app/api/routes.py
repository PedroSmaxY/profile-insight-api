from fastapi import APIRouter
from ..services.prolog_service import PrologService

routes = APIRouter()
prolog_service = PrologService()  # Criando uma única instância global



@routes.get("/questions/{perfil}/{num}")
async def get_questions(perfil: str, num: int):
    question = prolog_service.get_question(perfil, num)
    return {
        "perfil": perfil,
        "num": num,
        "question": question
    }
