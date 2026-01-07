from fastapi import FastAPI

from app.database.db_client import create_db_and_tables
from app.router.anomalieAdresse import router

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(router)
