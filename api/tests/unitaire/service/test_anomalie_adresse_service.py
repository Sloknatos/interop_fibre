import pytest
from app.error.exceptions import ExternalIDNotFound
from app.model.status import Status
from api.app.model.anomalie_adresse import AnomalieAdresse
from api.app.service.anomalie_adresse import AnomalieAdresseService


@pytest.fixture
def anomalie_adresse_service(mocker, session):
    manager = mocker.MagicMock()
    mocker.patch(
        "app.service.anomalieAdresse.AnomalieAdresseManager",
        return_value=manager,
    )
    service = AnomalieAdresseService(session)
    yield service


def describe_anomalie_adresse_service():
    def describe_init():
        def it_create_classe(mocker, session):
            manager = mocker.MagicMock()
            mocker.patch(
                "app.service.anomalieAdresse.AnomalieAdresseManager",
                return_value=manager,
            )
            service = AnomalieAdresseService(session)

            assert service.session == session
            assert service.anomalie_adresse_manager == manager

        def it_raise_error(mocker, session):
            with pytest.raises(TypeError):
                AnomalieAdresseService()

    def describe_create_anomalie():
        def it_raise_value_error(anomalie_adresse_service):
            anomalie_model = AnomalieAdresse()
            with pytest.raises(ValueError):
                anomalie_adresse_service.create_anomalie(anomalie_model)

        def it_create_anomalie(anomalie_adresse_service):
            anomalie_model = AnomalieAdresse(
                status="status", priority="priority", code_oi="code_oi"
            )
            anomalie_expect = AnomalieAdresse(
                status=Status.ACKNOWLEDGED,
                priority="priority",
                code_oi="code_oi",
            )

            anomalie_adresse_service.create_anomalie(anomalie_model)

            anomalie_adresse_service.anomalie_adresse_manager.create_anomalieAdresse.assert_called_once_with(
                anomalie_expect
            )

    def describe_read_anomalie():
        def it_return_anomalie(anomalie_adresse_service):
            anomalie_adresse_service.anomalie_adresse_manager.read_one_anomalie.return_value = "result"
            assert (
                anomalie_adresse_service.read_one_anomalie("test") == "result"
            )

        def it_raise_external_id_error(anomalie_adresse_service):
            anomalie_adresse_service.anomalie_adresse_manager.read_one_anomalie.side_effect = ExternalIDNotFound
            with pytest.raises(ExternalIDNotFound):
                anomalie_adresse_service.read_one_anomalie("test")

    def describe_cancel_anomalie():
        def it_cancel_anomalie(anomalie_adresse_service):
            anomalie_adresse_service.cancel_anomalie("test")
            anomalie_adresse_service.anomalie_adresse_manager.cancel_anomalie.assert_called_once_with(
                "test"
            )
