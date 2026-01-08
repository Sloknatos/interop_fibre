from typing import Annotated
from fastapi import Depends
from sqlmodel import Session

from app.database.db_client import get_session
from app.error.exceptions import ExternalIDNotFound
from app.model.anomalieAdresse import AnomalieAdresse
from app.model.status import Status
from app.database.anomalieAdresseManager import AnomalieAdresseManager


class AnomalieAdresseService:
    SessionDep = Annotated[Session, Depends(get_session)]

    def __init__(self, session: Session):
        self.session = session
        self.anomalie_adresse_manager = AnomalieAdresseManager(self.session)

    def create_anomalie(
        self, anomalie_adresse: AnomalieAdresse
    ) -> AnomalieAdresse:
        # Fields validation
        mandatory_fields = ["status", "priority", "code_oi"]
        print(anomalie_adresse)
        for field in mandatory_fields:
            print(field)
            if not anomalie_adresse.__getattribute__(field):
                raise ValueError(f"The field {field} is mandatory")

        # to follow rules : set status
        anomalie_adresse.status = Status.ACKNOWLEDGED

        # Put in DB
        return self.anomalie_adresse_manager.create_anomalieAdresse(
            anomalie_adresse
        )

    def read_one_anomalie(self, external_id: str) -> AnomalieAdresse:
        anomalie = self.anomalie_adresse_manager.read_one_anomalie(external_id)
        if anomalie:
            return anomalie
        else:
            raise ExternalIDNotFound("External ID not found")

    def cancel_anomalie(self, external_id: str) -> AnomalieAdresse:
        return self.anomalie_adresse_manager.cancel_anomalie(external_id)
