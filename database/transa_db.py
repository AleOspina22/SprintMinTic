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
    transfe: int
    regtransa: datetime
    presupuesto: salarioin + inversionesin + otrosin + (transfe)
    gasto: cbanout + efectivout + creditout

database_transa = Dict[int, TransaDB]
database_transa = {
}
