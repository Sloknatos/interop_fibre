import pytest
from app.model.status import Status
from app.error.exceptions import AnomalieCanceled, ExternalIDNotFound
from app.database.anomalieAdresseManager import AnomalieAdresseManager


def describe_anomalie_adresse_manager():
    def describe_init():
        def it_create(mocker):
            anomalie = AnomalieAdresseManager(mocker)
            assert anomalie
            assert anomalie.session == mocker
        def it_fail():
            with pytest.raises(TypeError) as exc_info:
                anomalie = AnomalieAdresseManager()
            assert exc_info.value.__str__() == "AnomalieAdresseManager.__init__() missing 1 required positional argument: 'session'"
            
    def describe_creation():
        def it_create(mocker, session):
            anomalie = AnomalieAdresseManager(session)
            result = anomalie.create_anomalieAdresse(mocker)
            
            session.add.assert_called_once()
            session.commit.assert_called_once()
            session.refresh.assert_called_once()

            assert result == mocker
            
    def describe_read_one_anomalie():
        def it_read_one_item(session, mocker):
            anomalie = AnomalieAdresseManager(session)
            session.exec.return_value.first.return_value = True
            anomalie.read_one_anomalie(mocker)            
            session.exec.assert_called_once()
    
    def describe_cancel_anomalie():
        def it_cancel_item(session, mocker):
            anomalie = AnomalieAdresseManager(session)
            anomalie.cancel_anomalie(mocker)
            
            anomalie_mock = mocker.MagicMock(name='anomalie')
            anomalie_mock.status.return_value = 'READY'
            session.exec.return_value.first.return_value = anomalie_mock
            
            session.exec.assert_called_once()
         
        def it_raise_external_id(session, mocker):
            anomalie = AnomalieAdresseManager(session)
            session.exec.return_value.first.return_value = None

            with pytest.raises(ExternalIDNotFound):
                anomalie.cancel_anomalie(mocker)
            
            session.exec.assert_called_once()
         
        def it_raise_anomalie_canceled(session, mocker, anomalie_canceled):
            anomalie = AnomalieAdresseManager(session)
            session.exec.return_value.first.return_value = anomalie_canceled

            with pytest.raises(AnomalieCanceled):
                anomalie.cancel_anomalie(mocker)

            session.exec.assert_called_once()
            