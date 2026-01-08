from fastapi import FastAPI

from app.utils.settings import settings
from app.database.db_client import create_db_and_tables
from app.router.anomalie_adresse import router


app = FastAPI(openapi_url=settings.openapi_url)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(router)
