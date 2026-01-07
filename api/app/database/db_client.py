from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine

from app.utils.settings import settings

database_url = f"sqlite:////{settings.sqlite_path}"
connect_args = {"check_same_thread": False}
engine = create_engine(database_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
