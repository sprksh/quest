
class BankingSystem:
    bank_map = {}
    
    @staticmethod
    def register_bank(bank):
        BankingSystem.bank_map[bank.bank_id] = bank
    
    @staticmethod
    def get_bank(bank_id):
        return BankingSystem.bank_map.get(bank_id)

    @staticmethod
    def _verify_account(bank, account_id, last_name):
        return bank.verify_account(account_id, last_name)

    @staticmethod
    def _withdraw(bank, account_id, amount):
        trxn = bank.transact(account_id, amount, trxn_type='withdraw')
        return trxn
    
    @staticmethod
    def atm_withdraw(bank_id, account_id, last_name, amount):
        bank = BankingSystem.get_bank(bank_id)
        if bank and BankingSystem._verify_account(bank, account_id, last_name):
            trxn = BankingSystem._withdraw(bank, account_id, amount)
            return trxn
        return

    @staticmethod
    def check_balance(bank_id, account_id, last_name):
        bank = BankingSystem.get_bank(bank_id)
        if bank and BankingSystem._verify_account(bank, account_id, last_name):
            return bank.check_balance(account_id)
        return
