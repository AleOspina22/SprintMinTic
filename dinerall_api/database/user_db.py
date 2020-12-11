from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    mail: str #pienso que es mejor por correo porque no le veo la finalidad a que los usuarios tengan un seudonimo dado que no tienen interaccion entre ellos, sin embargo, lo dejo por si algo sale mal
    password: str

database_users = Dict[str, UserInDB]
database_users = {
    "prueba1": UserInDB(**{"username":"prueba1","mail":"prueba1@mail.com","password":"prueba1"}),
    "prueba2": UserInDB(**{"username":"prueba2","mail":"prueba2@mail.com","password":"prueba2"}),
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