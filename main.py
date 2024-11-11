from fastapi import FastAPI
from app.api.routes import routes

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="profile-insight-api",
    version="1.0.1",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"hello": "Welcome to profile-insight-api!"}


app.include_router(routes, prefix="/api/v1")
