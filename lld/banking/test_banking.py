from .bank import Bank
from .atm import ATM
from .counter import BankCounter


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


if __name__ == "__main__":
    test_single_bank()
