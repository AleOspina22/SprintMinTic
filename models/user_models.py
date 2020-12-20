from pydantic import BaseModel
from datetime import date

class UserIn(BaseModel):
    name:str
    mail: str
    password:str
    birthday: date
    gender: str

class UserOut(BaseModel):
    name:str
    mail: str
    birthday: date
    gender: str
