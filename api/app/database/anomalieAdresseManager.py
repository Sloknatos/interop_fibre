from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, select

from api.app.error.exceptions import AnomalieCanceled, ExternalIDNotFound
from api.app.model.status import Status
from api.app.database.db_client import get_session
from api.app.model.anomalieAdresse import AnomalieAdresse


class AnomalieAdresseManager:
    SessionDep = Annotated[Session, Depends(get_session)]

    def __init__(self, session: SessionDep):
        self.session = session

    def create_anomalieAdresse(
        self, anomalie_adresse: AnomalieAdresse
    ) -> AnomalieAdresse:
        self.session.add(anomalie_adresse)
        self.session.commit()
        self.session.refresh(anomalie_adresse)
        return anomalie_adresse

    def read_one_anomalie(self, external_id: str) -> AnomalieAdresse:
        statement = select(AnomalieAdresse).where(
            AnomalieAdresse.external_id == external_id
        )
        return self.session.exec(statement).first()

    def cancel_anomalie(self, external_id: str) -> AnomalieAdresse:
        statement = select(AnomalieAdresse).where(
            AnomalieAdresse.external_id == external_id
        )
        anomalie_adresse = self.session.exec(statement).first()
        if not anomalie_adresse:
            raise ExternalIDNotFound("External ID not found")
        if anomalie_adresse.status == Status.CANCELED:
            raise AnomalieCanceled("Anomalie already cancelled")

        anomalie_adresse.status = Status.CANCELED
        return anomalie_adresse
