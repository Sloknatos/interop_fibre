from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from api.app.error.exceptions import AnomalieCanceled, ExternalIDNotFound
from api.app.model.anomalieAdresse import AnomalieAdresse
from api.app.database.db_client import get_db
from api.app.service.anomalieAdresse import AnomalieAdresseService

router = APIRouter(prefix="/anomalie-adresse'", tags=["TroubleTicket"])

# TODO make the error


@router.post("")
def create_anomalie_adresse(
    anomalie_adresse: AnomalieAdresse, session: Session = Depends(get_db)
) -> AnomalieAdresse | JSONResponse:
    anomalie_adresse_service = AnomalieAdresseService(session)
    try:
        return anomalie_adresse_service.create_anomalie(anomalie_adresse)
    except ValueError as exc:
        return JSONResponse(status_code=400, content={"message": exc.__str__()})
    except Exception as exc:
        return JSONResponse(status_code=500, content={"message": exc.__str__()})


@router.get("/{AnomalieAdresseId}")
def read_anomalie_adresse(
    AnomalieAdresseId: str, session: Session = Depends(get_db)
) -> AnomalieAdresse | JSONResponse:
    anomalie_adresse_service = AnomalieAdresseService(session)
    try:
        return anomalie_adresse_service.read_one_anomalie(AnomalieAdresseId)
    except ExternalIDNotFound as exc:
        return JSONResponse(status_code=404, content={"message": exc.__str__()})
    except Exception as exc:
        return JSONResponse(status_code=500, content={"message": exc.__str__()})


# Just cancellation for the moment, should deny service for other patch, Promise refacto
@router.patch("/{AnomalieAdresseId}")
def patch_anomalie_adresse(
    AnomalieAdresseId: str, session: Session = Depends(get_db)
) -> AnomalieAdresse:
    anomalie_adresse_service = AnomalieAdresseService(session)
    try:
        return anomalie_adresse_service.cancel_anomalie(AnomalieAdresseId)
    except ExternalIDNotFound as exc:
        return JSONResponse(status_code=400, content={"message": exc.__str__()})
    except AnomalieCanceled as exc:
        return JSONResponse(status_code=409, content={"message": exc.__str__()})
    except Exception as exc:
        return JSONResponse(status_code=418, content={"message": exc.__str__()})
