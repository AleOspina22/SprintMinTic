from pydantic import BaseModel

class AccountIn(BaseModel):
    user_mail: str
    name: str
    type: str
    balance: float

class AccountOut(BaseModel):
    user_mail: str
    name: str    
    type: str    
    balance: float