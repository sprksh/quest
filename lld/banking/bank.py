"""
Requirements:
1. A Bank capable of handling multiple people's accounts
2. System should be able to handle multiple Banks
3. ATMs Running in multiple threads/processes interacting to the bank



Bank:
    Should give an interface to register User
    Should give an interface to check balance for accoount
    Should give an interface to withdraw and deposit

"""
import random
import threading
import datetime
from lld.banking.banking_system import BankingSystem


class User:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.accounts = []

    def __repr__(self):
        return f"Name: {self.first_name} {self.last_name}"


class Account:
    def __init__(self, account_id, user, bank):
        self.account_id = account_id
        self.user = user
        self.balance = 0
        self.bank = bank
        self.transactions = []
    
    def __repr__(self):
        return "account ID: %s \n User: %s \n Balance: %s" % (self.account_id, self.user, self.balance)


class Transaction:
    def __init__(self, account_id, amount: float):
        self.account_id = account_id
        self.amount = amount
        self.timestamp = datetime.datetime.now()
    
    def __repr__(self):
        return f"Rs: {abs(self.amount)}, {'Credit' if self.amount < 0 else 'Debit'}, time: {self.timestamp}"


class Bank:
    def __init__(self, name: str, location: str, bank_id: int):
        self.name = name
        self.bank_id = bank_id
        self.location = location
        self.accounts = []
        self.account_map = {}
        self.vault = 0
        self.lock = threading.Lock()

    @staticmethod
    def bank_factory(name, location, bank_id):
        if bank_id in BankingSystem.bank_map:
            print("ID already exists")
            return
        bank = Bank(name, location, bank_id)
        Bank.register_bank_with_banking_system(bank)
        return bank

    @staticmethod
    def register_bank_with_banking_system(bank):
        BankingSystem.register_bank(bank)
        print("Bank registered with central banking system")

    def __repr__(self):
        return "Name: %s-%s, Id: %s" % (self.name, self.location, self.bank_id)

    def register_user(self, first_name, last_name, age):
        user = User(first_name, last_name, age)
        print(f"Created User: {user}")
        account = self._create_account(user)

        self.accounts.append(account)
        self.account_map[account.account_id] = account
        return account

    def _create_account(self, user):
        uid = random.randint(10000, 99999)
        account = Account(user=user, account_id=uid, bank=self)
        return account
    
    def verify_account(self, account_id, last_name):
        account = self.account_map.get(account_id)
        if account and account.user.last_name == last_name:
            return True
        return False

    def check_account_exists(self, account_id):
        if account_id in self.account_map:
            return True
        return False

    def transact(self, account_id, amount: float, trxn_type: str):
        account = self.account_map.get(account_id)
        if trxn_type == 'withdraw':
            with self.lock:
                if account.balance >= amount and self.check_vault_balance() >= amount:
                    import time; time.sleep(0.01)
                    return self._withdraw(account, amount)
                else:
                    print(f'Sorry, Transaction denied')
                    return None

        if trxn_type == 'deposit':
            return self._deposit(account, amount)
    
    def _withdraw(self, account, amount):
        self.vault -= amount
        trxn = Transaction(account_id=account.account_id, amount=-amount)
        account.balance -= amount
        account.transactions.append(trxn)
        self.check_vault_balance()
        self.check_balance(account.account_id)
        return trxn

    def _deposit(self, account, amount):
        self.vault += amount
        trxn = Transaction(account_id=account.account_id, amount=amount)
        account.balance += amount
        account.transactions.append(trxn)
        return trxn
    
    def _get_from_vault(self, amount):
        self.vault -= amount

    def check_vault_balance(self):
        if self.vault < 0:
            print(f"-------Current balance of bank {self} : {self.vault}")
        return self.vault

    def check_balance(self, account_id):
        account = self.account_map.get(account_id)
        if account:
            if account.balance < 0:
                print(f"--------Current acc balance {account_id}: {account.balance}")
            print(f"Current balance for account {account_id}: {account.balance}")
            return account.balance
