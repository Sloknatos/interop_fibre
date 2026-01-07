from pydantic import field_validator
from sqlmodel import SQLModel, Field
from datetime import datetime

from .status import Status
from .priority import Priority
from .ticketType import TicketType
from app.utils.regex_checker import is_code_check_regex


class AnomalieAdresse(SQLModel):
    __tablename__ = "anomalieAdresse"
    id: str | None = Field(default=None, primary_key=True)
    status: Status = Field(default=Status.ACKNOWLEDGED)
    status_change_details: str = Field(default="")
    description: str = Field(default="")
    external_Dd: str = Field(default="")
    priority: Priority = Field()

    # relatedEntity: dict #RelatedBuilding : should implement more models
    # relatedParty: list #relatedEntity : same

    requested_Resolution_date: datetime = Field(default=datetime.now)
    severity: str = Field(default="")

    ticket_type: TicketType = Field()
    # statusChangeReason: dict # no more info in swagger, is this something as key, value where key = datatime of change and value = str with human readable reason ?

    code_oi: str = Field(default="")
    code_oc: str = Field(default="")
    siren: str = Field(default="")
    siret: str = Field(default="")

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
