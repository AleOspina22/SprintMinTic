from pydantic import BaseModel


class AccountInDB(BaseModel):
    id_account: int=0
    user_mail: str
    name: str    # Débito, Nequi, Ahorro, etc
    type: str    # Cuenta bancaria, Ahorro o inversiones, Otras
    balance: float=0

database_accounts = [str, AccountInDB]
generator = {"id": 0}





