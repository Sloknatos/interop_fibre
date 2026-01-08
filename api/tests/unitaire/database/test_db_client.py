from unittest.mock import MagicMock
from sqlmodel import SQLModel, Session
from app.database.db_client import create_db_and_tables, get_session


def describe_db_client():
    
    def describe_create_db_and_tables():
        def called_once(mocker):
            mocker.patch(
                'app.database.db_client.SQLModel.metadata.create_all',
            )            
            create_db_and_tables()
            SQLModel.metadata.create_all.assert_called_once()
