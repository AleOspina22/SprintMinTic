from pydantic import BaseModel

class AccountIn(BaseModel):
    user_mail: str
    name: str
    type: str
    balance: float

class AccountOut(BaseModel):
    id_account: int
    user_mail: str
    name: str    
    type: str    
    balance: float