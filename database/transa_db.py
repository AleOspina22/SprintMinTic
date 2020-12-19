from typing import Dict
from pydantic import BaseModel
from date import datetime
from models.transa_models import

class TransaDB(BaseModel):
    salarioin: int
    inversionesin: int
    otrosin: int
    cbanout: int
    efectivout: int
    creditout: int
    regtransa: datetime

database_transa = Dict[int, TransaDB]
database_transa = {
}