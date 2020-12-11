from pydantic import BaseModel

class UserIn(BaseModel):
    username:str
    mail: str
    password:str
    

class UserOut(BaseModel):
    username:str