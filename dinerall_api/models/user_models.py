from pydantic import BaseModel

class UserIn(BaseModel):
    mail: str
    password:str

class UserNew(BaseModel):
    name:str
    mail: str
    password:str
    birthday: datetime.date
    gender: str

class UserNew(BaseModel):
    name:str
    mail: str
    birthday: datetime.date
    gender: str
