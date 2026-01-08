import pytest
from unittest.mock import MagicMock

from api.app.model.anomalie_adresse import AnomalieAdresse
from app.model.status import Status
from app.main import app


@pytest.fixture
def session():
    session = MagicMock(name="session")
    session.add.return_value = True
    session.commit.return_value = True
    session.refresh.return_value = True
    yield session


@pytest.fixture
def anomalie_canceled():
    anomalie = AnomalieAdresse(status=Status.CANCELED)
    yield anomalie


@pytest.fixture
def fixture_app():
    return app
