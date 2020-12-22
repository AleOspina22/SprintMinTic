from typing import Dict
from pydantic import BaseModel

from models.account_models import AccountIn

class AccountInDB(BaseModel):
    user_mail: str
    name: str    # Efectivo, Débito, Nequi, Ahorro, etc
    category: str='Cuenta bancaria'  # Cuenta bancaria, efectivo, ahorro o inversiones, Otras
    balance: float=0

database_accounts = Dict[str, Dict[str, AccountInDB]]
database_accounts = {
        "carlos@gmail.com": {"Billetera": AccountInDB(**{'user_mail': "carlos@gmail.com",
                                                        'name': 'Billetera',   
                                                        'category': 'Efectivo',
                                                        'balance': 120000.0}),
                                                        
                             "Debito": AccountInDB(**{'user_mail': "carlos@gmail.com",
                                                        'name': 'Debito',   
                                                        'category': 'Cuenta bancaria',
                                                        'balance': 550000.0})
         },

        "veronica@gmail.com": {"Billetera": AccountInDB(**{'user_mail': "veronica@gmail.com",
                                                        'name': 'Billetera',   
                                                        'category': 'Efectivo',
                                                        'balance': 300000.0})
         },

        "james@gmail.com": {"Billetera": AccountInDB(**{'user_mail': "james@gmail.com",
                                                        'name': 'Billetera',   
                                                        'category': 'Efectivo',
                                                        'balance': 45000.0}),
                                                        
                             "Ahorro": AccountInDB(**{'user_mail': "james@gmail.com",
                                                        'name': 'Ahorro',   
                                                        'category': 'Cuenta bancaria',
                                                        'balance': 1800000.0}),

                             "Nequi": AccountInDB(**{'user_mail': "james@gmail.com",
                                                        'name': 'Nequi',   
                                                        'category': 'Cuenta bancaria',
                                                        'balance': 220000.0})
         }
}


# Función para obtener las cuentas de un usuario
def get_accounts(mail: str):
    if mail in database_accounts.keys():
        return database_accounts[mail]
    else: 
        return None

# Función para crear/actualizar el usuario
def save_new_user(mail: str):
    default_account = {"Billetera": AccountInDB(**{'user_mail': mail,
                                                        'name': 'Billetera',   
                                                        'category': 'Efectivo',
                                                        'balance': 0.0})
    }
    database_accounts.update({mail: default_account})
    return database_accounts[mail]



# Función para crear/actualizar el usuario
def save_account(account_in_db: AccountIn):
    user_mail = account_in_db.user_mail
    account_name = account_in_db.name

    if account_name in list(database_accounts[user_mail].keys()):
        return None
    else:
        database_accounts[user_mail][account_name] = AccountInDB(**account_in_db.dict())
        return account_in_db



