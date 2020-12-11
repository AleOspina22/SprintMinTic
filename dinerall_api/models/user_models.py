from pydantic import BaseModel
from datetime import date

class UserIn(BaseModel):
    mail: str
    password:str

class UserNew(BaseModel):
    name:str
    mail: str
    password:str
    birthday: date
    gender: str

class UserOut(BaseModel):
    name:str
    mail: str
