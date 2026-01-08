from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.error.exceptions import AnomalieCanceled, ExternalIDNotFound
from app.model.anomalie_adresse import AnomalieAdresse
from app.database.db_client import get_session
from app.service.anomalie_adresse import AnomalieAdresseService

router = APIRouter(prefix="/anomalie-adresse", tags=["TroubleTicket"])


@router.post(
    "/",
    response_model=AnomalieAdresse,
    description="Create a trouble ticket",
    summary="Create a trouble ticket",
    )
def create_anomalie_adresse(
    anomalie_adresse: AnomalieAdresse, session: Session = Depends(get_session)
):
    try:
        anomalie_adresse_service = AnomalieAdresseService(session)
        return anomalie_adresse_service.create_anomalie(anomalie_adresse)
    except ValueError as exc:
        return JSONResponse(status_code=400, content={"message": exc.__str__()})
    except Exception as exc:
        return JSONResponse(status_code=500, content={"message": exc.__str__()})


@router.get(
    "/{AnomalieAdresseId}",
    description="Get a trouble ticket",
    summary="Get a trouble ticket",
    )
def read_anomalie_adresse(
    AnomalieAdresseId: str, session: Session = Depends(get_session)
):
    try:
        anomalie_adresse_service = AnomalieAdresseService(session)
        return anomalie_adresse_service.read_one_anomalie(AnomalieAdresseId)
    except ExternalIDNotFound as exc:
        return JSONResponse(status_code=404, content={"message": exc.__str__()})
    except Exception as exc:
        return JSONResponse(status_code=500, content={"message": exc.__str__()})


# Just cancellation for the moment, should deny service for other patch, Promise refacto
@router.patch(
    "/{AnomalieAdresseId}",
    description="Partially update a trouble ticket",
    summary="Partially update a trouble ticket",
    )
def patch_anomalie_adresse(
    AnomalieAdresseId: str, session: Session = Depends(get_session)
):
    try:
        anomalie_adresse_service = AnomalieAdresseService(session)
        return anomalie_adresse_service.cancel_anomalie(AnomalieAdresseId)
    except ExternalIDNotFound as exc:
        return JSONResponse(status_code=400, content={"message": exc.__str__()})
    except AnomalieCanceled as exc:
        return JSONResponse(status_code=409, content={"message": exc.__str__()})
    except Exception as exc:
        return JSONResponse(status_code=418, content={"message": exc.__str__()})
