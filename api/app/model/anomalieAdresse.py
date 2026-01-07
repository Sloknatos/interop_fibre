from pydantic import field_validator
from sqlmodel import SQLModel, Field
from datetime import datetime

from .status import Status
from .priority import Priority
from .ticketType import TicketType
from app.utils.regex_checker import is_code_check_regex


class AnomalieAdresse(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    status: Status = Field(default=Status.ACKNOWLEDGED)
    status_change_details: str | None = Field(default=None)
    description: str | None = Field(default=None)
    external_id: str | None = Field(default=None)
    priority: Priority = Field(default=Priority.LOW)

    # relatedEntity: dict #RelatedBuilding : should implement more models
    # relatedParty: list #relatedEntity : same

    requested_Resolution_date: datetime | None = Field(default=None)
    severity: str | None = Field(default=None)

    ticket_type: TicketType | None = Field(default=TicketType.CUSTOMER_REQUEST)
    # statusChangeReason: dict # no more info in swagger, is this something as key, value where key = datatime of change and value = str with human readable reason ?

    code_oi: str = Field(default="FETL")
    code_oc: str | None = Field(default=None)
    siren: str | None = Field(default=None)
    siret: str | None = Field(default=None)

    @field_validator("code_oi")
    @classmethod
    def code_oi_pattern_compliance(cls, code: str) -> str:
        if not is_code_check_regex(code):
            raise ValueError("code do not match regex")
        return code.title()

    @field_validator("code_oc")
    @classmethod
    def code_oc_pattern_compliance(cls, code: str) -> str:
        if not is_code_check_regex(code):
            raise ValueError("code do not match regex")
        return code.title()


"""
TODO remove
class AnomalieAdresseBase(BaseModel):
    status: Status
    statusChangeDetails: str
    description: str
    externalId: str
    priority: Priority
    relatedEntity: dict #RelatedBuilding
    relatedParty: list #relatedEntity
    requestedResolutionDate: datetime
    severity: str
    ticketType: TicketType
    statusChangeReason: dict #no more info in swagger
    code_oi: str
    code_oc: str
    siren: str
    siret: str
    
    model_config = ConfigDict(from_attributes=True)
    
    
    
class AnomalieAddresseCreation(AnomalieAdresseBase):
    status: Status = Status.ACKNOWLEDGED
"""
