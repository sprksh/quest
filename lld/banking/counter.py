
class BankCounter:
    def __init__(self, bank):
        self.bank = bank

    def withdraw(self, account_id, last_name, amount):
        if self.bank.verify_account(account_id, last_name):
            self.bank.transact(account_id, amount, trxn_type='withdraw')
        else:
            print("Error!")
    
    def deposit(self, account_id, amount):
        if self.bank.check_account_exists(account_id):
            self.bank.transact(account_id, amount, trxn_type='deposit')
        else:
            print("Account ID is wrong")

    def open_account(self, first_name, last_name, age):
        account = self.bank.register_user(first_name, last_name, age)
        return account.account_id
    
    def check_balance(self, account_id, last_name):
        if self.bank.verify_account(account_id, last_name):
            return self.bank.check_balance(account_id)
        print("Account ID is wrong")
