from typing import Dict
from pydantic import BaseModel

class AccountInDB(BaseModel):
    id_account: int=0
    user_mail: str
    name: str    # Efectivo, Débito, Nequi, Ahorro, etc
    category: str='Cuenta de ahorro'  # Cuenta bancaria, efectivo, ahorro o inversiones, Otras
    balance: float=0

generator = {"id": 0}

database_accounts = Dict[str, Dict[str, AccountInDB]]
database_accounts = {
        "carlos@gmail.com": {"Billetera": AccountInDB(**{user_mail: "carlos@gmail.com",
                                                        name: 'Billetera',   
                                                        category: 'Efectivo',
                                                        balance: 120000.0}),
                                                        
                             "Debito": AccountInDB(**{user_mail: "carlos@gmail.com",
                                                        name: 'Debito',   
                                                        category: 'Cuenta bancaria',
                                                        balance: 550000.0})
         },

        "veronica@gmail.com": {"Billetera": AccountInDB(**{user_mail: "veronica@gmail.com",
                                                        name: 'Billetera',   
                                                        category: 'Efectivo',
                                                        balance: 300000.0})
         },

        "james@gmail.com": {"Billetera": AccountInDB(**{user_mail: "james@gmail.com",
                                                        name: 'Billetera',   
                                                        category: 'Efectivo',
                                                        balance: 45000.0}),
                                                        
                             "Ahorro": AccountInDB(**{user_mail: "james@gmail.com",
                                                        name: 'Ahorro',   
                                                        category: 'Cuenta bancaria',
                                                        balance: 1800000.0}),

                             "Nequi": AccountInDB(**{user_mail: "james@gmail.com",
                                                        name: 'Nequi',   
                                                        category: 'Cuenta bancaria',
                                                        balance: 220000.0})
         }
}



def create_account(account_in_db: AccountInDB):
    generator["id"] = generator["id"] + 1
    account_in_db.id_transaction = generator["id"]


def update_account(account_in_db: AccountInDB):
    generator["id"] = generator["id"] + 1
    account_in_db.id_transaction = generator["id"]




