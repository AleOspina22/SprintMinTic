from pydantic import BaseModel

class TransaNew(BaseModel):
    salarioin: int
    inversionesin: int
    otrosin: int
    cbanout: int
    efectivout: int
    creditout: int
    transfe: int


class TransaOut(BaseModel):
    presupuesto: int
    gasto: int