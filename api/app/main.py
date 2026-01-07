from fastapi import FastAPI

from app.router import anomalie_adresse_router

app = FastAPI()
app.include_router(anomalie_adresse_router)
