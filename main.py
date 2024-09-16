from fastapi import FastAPI
from app.api.routes import routes


app = FastAPI(
    title="profile-insight-api",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

app.include_router(routes, prefix="/api/v1")
