from enum import Enum

class TicketType(str, Enum):
    CUSTOMER_REQUEST = 'CUSTOMER_REQUEST'
    OC_REQUEST = 'OC_REQUEST'