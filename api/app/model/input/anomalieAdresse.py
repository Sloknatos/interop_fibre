from pydantic import BaseModel, field_validator

from datetime import datetime

from .status import Status
from .priority import Priority
from .ticketType import TicketType
from app.utils.regex_checker import is_code_check_regex

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
    
    @field_validator('code_oi')
    @classmethod
    def code_oi_pattern_compliance(cls, code: str) -> str:
        if not is_code_check_regex(code):
            raise ValueError('code do not match regex')
        return code.title()
    
    @field_validator('code_oc')
    @classmethod
    def code_oc_pattern_compliance(cls, code: str) -> str:
        if not is_code_check_regex(code):
            raise ValueError('code do not match regex')
        return code.title()
    
class AnomalieAddresseCreation(AnomalieAdresseBase):
    status: Status = Status.ACKNOWLEDGED
