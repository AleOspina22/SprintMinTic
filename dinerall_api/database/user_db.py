from typing import Dict
from pydantic import BaseModel
import datetime

class UserInDB(BaseModel):
    name: str
    mail: str #pienso que es mejor por correo porque no le veo la finalidad a que los usuarios tengan un seudonimo dado que no tienen interaccion entre ellos, sin embargo, lo dejo por si algo sale mal
    password: str
    birthday: datetime.date
    gender: str

database_users = Dict[str, UserInDB]
database_users = {
    "carlos@gmail.com": UserInDB(**{"name":"Carlos",
                            "mail":"carlos@gmail.com",
                            "password":"carlos12345"}),
    "veronica@gmail.com": UserInDB(**{"name":"Veronica",
                            "mail":"veronica@gmail.com",
                            "password":"veronica12345"}),
    "james@gmail.com": UserInDB(**{"name":"James",
                            "mail":"james@gmail.com",
                            "password":"james12345"}),
}
#funcion de loguear
def login(mail:str,password:str):
    if mail and password in database_users.keys():
        return "Se ha logueado correctamente. Bienvenido a Dinerall "+database_users[mail]+"."
    else:
        return "Usuario o contraseña incorrectos. Pruebe nuevamente o regístrese."


def signup(name:str,mail:str,password:str, birthday:datetime.date,gender:str):
    name=input[database_users[name]]
    mail=input[database_users[mail]]
    password=input[database_users[password]]
    birthday=input[database_users[birthday]]
    gender=input[database_users[gender]]
    return "Usuario registrado correctamente."
