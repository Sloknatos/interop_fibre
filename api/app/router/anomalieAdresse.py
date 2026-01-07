from fastapi import APIRouter

from app.model.input.anomalieAdresse import AnomalieAdresse, AnomalieAddresseCreation

router = APIRouter(prefix="/anomalie-adresse'", tags=['TroubleTicket'])


@router.post('')
def create_anomalie_adresse(anomalieAdresse: AnomalieAddresseCreation) -> AnomalieAdresse:
    return anomalieAdresse

@router.get('/{AnomalieAdresseId}')
def read_anomalie_adresse(AnomalieAdresseId: str) -> AnomalieAdresse:
    return None

# Just for cancellation for the moment, should deny service for other patch, Promise refacto
@router.patch('/{AnomalieAdresseId}')
def patch_anomalie_adresse(AnomalieAdresseId: str) -> AnomalieAdresse:
    return None