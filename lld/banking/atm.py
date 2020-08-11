from lld.banking.banking_system import BankingSystem


class ATM:
    def __init__(self, id):
        self.id = id
    
    def run(self):
        pass

    def withdraw(self, bank_id, account_id, last_name, amount):
        return BankingSystem.atm_withdraw(bank_id, account_id, last_name, amount)
    
    def check_balance(self, bank_id, account_id, last_name):
        return BankingSystem.check_balance(bank_id, account_id, last_name)
