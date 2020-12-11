from fastapi import FastAPI, HTTPException
import datetime

from database.user_db import UserInDB
from database.user_db import get_user, save_user
from models.user_models import UserIn, UserNew, UserOut

api = FastAPI()

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):

    user_in_db = get_user(user_in.mail)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="No existe un regristado con el correo electrónico")

    if user_in_db.password != user_in.password:
        return {'Autenticación': False}

    return {"Autenticación": True}


@api.put("/user/signup/")
async def create_user(user_new: UserNew):

    user_in_db = get_user(user_new.email)
    if user_in_db != None:
        raise HTTPException(status_code=404, detail="El email ya está registrado.")

    user_new = save_user(user_new)
    user_out = UserOut(**user_new.dict())
    return user_out
