from .bank import Bank
from .atm import ATM
from .counter import BankCounter
import random
import threading


def test_single_bank():
    bank1 = Bank.bank_factory('SBI', 'Delhi', 1)
    counter1 = BankCounter(bank1)
    atm1 = ATM(1)

    first_name, last_name, age = 'Surya', 'Prakash', 28
    account1_id = counter1.open_account(first_name, last_name, age)
    counter1.check_balance(account1_id, last_name=last_name)
    
    counter1.deposit(account1_id, 10000.0)
    counter1.check_balance(account1_id, last_name=last_name)
    counter1.withdraw(account1_id, last_name, 1000.0)

    atm1.check_balance(bank1.bank_id, account1_id, last_name)
    atm1.withdraw(bank1.bank_id, account1_id, last_name, 1500.50)
    atm1.check_balance(bank1.bank_id, account1_id, last_name)
    counter1.check_balance(account1_id, last_name=last_name)
    counter1.deposit(account1_id, 1000.0)
    atm1.check_balance(bank1.bank_id, account1_id, last_name)
    atm1.withdraw(bank1.bank_id, account1_id, last_name, 3500)
    atm1.check_balance(bank1.bank_id, account1_id, last_name)


def test_multithreaded():
    bank = Bank.bank_factory('SBI', 'Delhi', 1)
    atm_id = random.randint(100, 300)
    atm1 = ATM(atm_id)

    def deposit_and_with_draw_in_loop(thread_id, bank):
        
        counter = BankCounter(bank)
        first_name, last_name, age = 'Surya', f'Prakash-{thread_id}', 28
        account_id = counter.open_account(first_name, last_name, age)
        account = bank.account_map[account_id]
        threads = []
        for i in range(100):
            args = (account_id, account)
            thread = threading.Thread(target=simulate_transactions, args=args)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        
        print(f"final value {account_id}")
        counter.check_balance(account_id, last_name=last_name)
        print("---------")
    
    def simulate_transactions(account_id, account):
        amount = random.randint(100, 500)
        # this one is original
        # counter.withdraw(account_id, last_name, amount)
        # counter.deposit(account_id, amount)

        # this one is another try to directly call bank's internal methods from the multiple threads
        w = False
        if bank.check_balance(account_id) >= amount:
            w = True
        else:
            print("transaction denied")
        if w:
            bank._withdraw(account, amount)
        amount = random.randint(100, 500)
        bank._deposit(account, amount)
        

    threads = []
    for i in range(5):
        args = (i, bank)
        thread = threading.Thread(target=deposit_and_with_draw_in_loop, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    
    print(f"Current Balance in bank vault {bank.check_vault_balance()}")

            
if __name__ == "__main__":
    test_single_bank()
