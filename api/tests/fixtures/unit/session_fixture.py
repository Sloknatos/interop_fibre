import pytest
from unittest.mock import MagicMock

@pytest.fixture
def session():
    session = MagicMock(name='session')
    session.add.return_value = True
    session.commit.return_value = True
    session.refresh.return_value = True
    yield session