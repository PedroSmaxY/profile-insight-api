from fastapi import APIRouter

routes = APIRouter()

@routes.get("/users/{id}")
async def get_users(item_id: int):
        return {"message": item_id}
