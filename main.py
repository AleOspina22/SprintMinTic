from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import datetime

# User
from database.user_db import UserInDB
from database.user_db import get_user, save_user
from models.user_models import UserIn, UserNew,  UserOut
# Report
from database.account_db import AccountInDB
from database.account_db import get_accounts, save_account, save_new_user
from models.account_models import AccountIn, AccountOut



api = FastAPI()


origins = [
    "http://localhost.tiangolo.com", 
    "https://localhost.tiangolo.com",
    "http://localhost", 
    "http://localhost:8080",
    "https://dinerall-app.herokuapp.com",
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.get("/")
async def read_root():
    return "Hi, welcome to Dinerall V2"

@api.post("/login/")
async def auth_user(user_in: UserIn):

    user_in_db = get_user(user_in.mail)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="No existe un regristado con el correo electrónico")

    if user_in_db.password != user_in.password:
        return False
    else:
        return True


@api.post("/signup/")
async def create_user(user_new: UserNew):

    user_in_db = get_user(user_new.mail)
    if user_in_db != None:
        raise HTTPException(status_code=404, detail="El email ya está registrado.")

    user_new = save_user(user_new)
    user_out = UserOut(**user_new.dict())

    #Creamos una cuenta default para el nuevo usuario
    user_account =  save_new_user(user_new.mail)
    return user_out


@api.get("/{mail}/balance/")
async def get_balance(mail: str): 

    accounts_in_db = get_accounts(mail)

    if accounts_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    balance_out = {}
    for key in accounts_in_db.keys():
        acc = AccountOut(**accounts_in_db[key].dict())
        balance_out.update({acc.name: acc.balance}) 

    return balance_out

@api.get("/{mail}/balance/list-accounts")
async def get_balance(mail: str): 

    accounts_in_db = get_accounts(mail)

    if accounts_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    return accounts_in_db

@api.post("/settings/accounts/new")
async def create_account(account_in: AccountIn):

    user_in_db = get_user(account_in.user_mail)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    account_in_db = AccountInDB(**account_in.dict())
    account_in_db = save_account(account_in_db)

    if account_in_db == None:
        raise HTTPException(status_code=404, detail="Ya existe una cuenta con el mismo nombre")

    return account_in_db 
