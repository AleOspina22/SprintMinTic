from pydantic import BaseModel

class AccountIn(BaseModel):
    user_mail: str
    name: str

class AccountOut(BaseModel):
    id_account: int=0
    user_mail: str
    name: str    
    type: str    
    balance: float=0