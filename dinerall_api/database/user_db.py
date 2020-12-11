from typing import Dict
from pydantic import BaseModel
import datetime

class UserInDB(BaseModel):
    name: str
    mail: str #pienso que es mejor por correo porque no le veo la finalidad a que los usuarios tengan un seudonimo dado que no tienen interaccion entre ellos, sin embargo, lo dejo por si algo sale mal
    password: str
    birthday: datetime
    gender: str

database_users = Dict[str, UserInDB]
database_users = {
    "Carlos": UserInDB(**{"username":"Carlos",
                            "mail":"carlos@gmail.com",
                            "password":"carlos12345"}),
    "Veronica": UserInDB(**{"username":"Veronica",
                            "mail":"veronica@gmail.com",
                            "password":"veronica12345"}),
    "James": UserInDB(**{"username":"James",
                            "mail":"james@gmail.com",
                            "password":"james12345"}),
}
#funcion de loguear
def login(username:str,password:str):
    if username and password in database_users.keys():
        return "Se ha logueado correctamente. Bienvenido a Dinerall "+database_users[username]+"."
    else:
        return "Usuario o contraseña incorrectos. Pruebe nuevamente o regístrese."
#funcion de registro, en esta no estoy muy seguro si esta bien, ya seria mirar en pruebas
def signin(username:str,mail:str,password:str):
    username=input[database_users[username]]
    mail=input[database_users[mail]]
    password=input[database_users[password]]
    return "Usuario registrado correctamente."
