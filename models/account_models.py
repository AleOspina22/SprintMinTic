from pydantic import BaseModel

class AccountIn(BaseModel):
    user_mail: str
    name: str
    category: str
    balance: float

class AccountOut(BaseModel):
    name: str
    balance: float