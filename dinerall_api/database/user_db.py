from typing import Dict
from pydantic import BaseModel
import datetime

class UserInDB(BaseModel):
    name: str
    mail: str #pienso que es mejor por correo porque no le veo la finalidad a que los usuarios tengan un seudonimo dado que no tienen interaccion entre ellos, sin embargo, lo dejo por si algo sale mal
    password: str
<<<<<<< HEAD
    birthday: datetime.date
=======
    birthday: datetime
>>>>>>> d852e7a7d356ce7d63676aeafa09db92e63c04b6
    gender: str

database_users = Dict[str, UserInDB]
database_users = {
    "Carlos": UserInDB(**{"name":"Carlos",
                            "mail":"carlos@gmail.com",
                            "password":"carlos12345"}),
    "Veronica": UserInDB(**{"name":"Veronica",
                            "mail":"veronica@gmail.com",
                            "password":"veronica12345"}),
    "James": UserInDB(**{"name":"James",
                            "mail":"james@gmail.com",
                            "password":"james12345"}),
}
#funcion de loguear
def login(mail:str,password:str):
    if mail and password in database_users.keys():
        return "Se ha logueado correctamente. Bienvenido a Dinerall "+database_users[mail]+"."
    else:
        return "Usuario o contraseña incorrectos. Pruebe nuevamente o regístrese."
#funcion de registro, en esta no estoy muy seguro si esta bien, ya seria mirar en pruebas
<<<<<<< HEAD
def signup(name:str,mail:str,password:str, birthday:datetime.date,gender:str):
    name=input[database_users[name]]
=======
def signup(username:str,mail:str,password:str):
    username=input[database_users[username]]
>>>>>>> d852e7a7d356ce7d63676aeafa09db92e63c04b6
    mail=input[database_users[mail]]
    password=input[database_users[password]]
    birthday=input[database_users[birthday]]
    gender=input[database_users[gender]]
    return "Usuario registrado correctamente."
