from typing import Dict
from pydantic import BaseModel
from datetime import date

from models.user_models import UserIn, UserNew, UserOut

class UserInDB(BaseModel):
    name: str
    mail: str
    password: str
    birthday: date
    gender: str

database_users = Dict[str, UserInDB]
database_users = {
    "carlos@gmail.com": UserInDB(**{"name":"Carlos",
                            "mail":"carlos@gmail.com",
                            "password":"carlos12345",
                            "birthday": date(2020, 12, 11),
                            "gender": "m"
                            }),
    "veronica@gmail.com": UserInDB(**{"name":"Veronica",
                            "mail":"veronica@gmail.com",
                            "password":"veronica12345",
                            "birthday": date(2020, 12, 11),
                            "gender": "m",
                            }),
    "james@gmail.com": UserInDB(**{"name":"James",
                            "mail":"james@gmail.com",
                            "password":"james12345",
                            "birthday": date(2020, 12, 11),
                            "gender": "m"
                            }),
}

# Función para loguear
def get_user(mail: str):
    if mail in database_users.keys():
        return database_users[mail]
    else:
        return None

# Función para guardar el usuario
def save_user(user_in_db: UserNew):
    mail = user_in_db.mail
    database_users[mail] = UserInDB(**user_in_db.dict())
    return user_in_db
