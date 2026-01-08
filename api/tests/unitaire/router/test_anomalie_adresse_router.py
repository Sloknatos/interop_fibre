from app.error.exceptions import AnomalieCanceled, ExternalIDNotFound
from app.router.anomalie_adresse import (
    create_anomalie_adresse,
    patch_anomalie_adresse,
    read_anomalie_adresse,
)


def describe_anomalie_adresse_router():
    def describe_create_anomalie_adresse():
        def it_return_anomalie(mocker):
            anomalie = mocker.patch(
                "app.router.anomalie_adresse.AnomalieAdresseService",
            )
            create_anomalie_adresse(mocker)
            anomalie.assert_called_once()

        def it_raise_value_error(mocker):
            mocker.patch(
                "app.router.anomalie_adresse.AnomalieAdresseService",
                side_effect=ValueError,
            )
            result = create_anomalie_adresse(mocker)
            assert result.status_code == 400

        def it_raise_other(mocker):
            mocker.patch(
                "app.router.anomalie_adresse.AnomalieAdresseService",
                side_effect=Exception,
            )
            result = create_anomalie_adresse(mocker)
            assert result.status_code == 500

    def describe_read_anomalie_adresse():
        def it_return_anomalie(mocker):
            anomalie = mocker.patch(
                "app.router.anomalie_adresse.AnomalieAdresseService",
            )
            read_anomalie_adresse(mocker)
            anomalie.assert_called_once()

        def it_raise_external_id_error(mocker):
            mocker.patch(
                "app.router.anomalie_adresse.AnomalieAdresseService",
                side_effect=ExternalIDNotFound,
            )
            result = read_anomalie_adresse(mocker)
            assert result.status_code == 404

        def it_raise_other(mocker):
            mocker.patch(
                "app.router.anomalie_adresse.AnomalieAdresseService",
                side_effect=Exception,
            )
            result = read_anomalie_adresse(mocker)
            assert result.status_code == 500

    def describe_patch_anomalie_adresse():
        def it_return_anomalie(mocker):
            anomalie = mocker.patch(
                "app.router.anomalie_adresse.AnomalieAdresseService",
            )
            patch_anomalie_adresse(mocker)
            anomalie.assert_called_once()

        def it_raise_external_id_error(mocker):
            mocker.patch(
                "app.router.anomalie_adresse.AnomalieAdresseService",
                side_effect=ExternalIDNotFound,
            )
            result = patch_anomalie_adresse(mocker)
            assert result.status_code == 400

        def it_raise_cancelled_error(mocker):
            mocker.patch(
                "app.router.anomalie_adresse.AnomalieAdresseService",
                side_effect=AnomalieCanceled,
            )
            result = patch_anomalie_adresse(mocker)
            assert result.status_code == 409

        def i_am_a_teapot(mocker):
            mocker.patch(
                "app.router.anomalie_adresse.AnomalieAdresseService",
                side_effect=Exception,
            )
            result = patch_anomalie_adresse(mocker)
            assert result.status_code == 418
