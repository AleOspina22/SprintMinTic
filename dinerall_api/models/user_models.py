from pydantic import BaseModel

class UserIn(BaseModel):
    name:str
    mail: str
    password:str
    

class UserOut(BaseModel):
    name:str