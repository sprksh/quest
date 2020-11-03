class User:
    def __init__(self, name, email, credit_limit):
        self.name = name
        self.email = email
        self.credit_limit = credit_limit
        self.residual_limit = credit_limit
        self.dues = 0
        self.transactions = []

    @staticmethod
    def user_factory(name, email, credit_limit):
        return User(name, email, credit_limit)

    def check_transaction_possible(self, amount):
        if amount > self.residual_limit:
            return False
        return True

    def handle_transaction(self, txn):
        self.transactions.append(txn)
        self.residual_limit -= txn.amount
        self.dues += txn.amount
    
    def handle_payback(self, amount):
        self.residual_limit = min(self.credit_limit, self.residual_limit + amount)
        self.dues -= amount


class Merchant:
    def __init__(self, name, email, discount):
        self.name = name
        self.email = email
        self.discount = discount
        self.transactions = []
        self.total_discount_given = 0

    @staticmethod
    def merchant_factory(name, email, discount):
        return Merchant(name, email, discount)

    def handle_transaction(self, txn):
        self.transactions.append(txn)
        self.total_discount_given += txn.discount_value

    def set_discount_percentage(self, discount_percentage):
        self.discount = discount_percentage


class Transaction:
    def __init__(self, user, merchant, amount):
        self.user = user
        self.merchant = merchant
        self.amount = amount
        self.discount_value = merchant.discount * amount / 100
