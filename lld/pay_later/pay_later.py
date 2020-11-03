from entities import User, Merchant, Transaction


class PayLaterService:
    def __init__(self):
        self.user_dict = {}
        self.merchants_dict = {}

    def get_user_by_name(self, name):
        return self.user_dict[name]

    def get_merchant_by_name(self, name):
        return self.merchants_dict[name]

    def register_user(self, name, email, credit_limit):
        user = User.user_factory(name, email, credit_limit)
        self.user_dict[name] = user
        return user

    def register_merchant(self, name, email, discount):
        merchant = Merchant(name, email, discount)
        self.merchants_dict[name] = merchant
        return merchant

    def change_merchant_discount(self, merchant, discount_percent):
        merchant.set_discount_percentage(discount_percent)
        return merchant

    def handle_transaction(self, user, merchant, amount):
        if not user.check_transaction_possible(amount):
            return "rejected! (reason: credit limit)"
        self._transact(user, merchant, amount)
        return "Success!"

    def _transact(self, user: User, merchant: Merchant, amount):
        txn = Transaction(user, merchant, amount)
        user.handle_transaction(txn)
        merchant.handle_transaction(txn)
        return txn

    def handle_payback(self, user: User, amount):
        user.handle_payback(amount)
        return user

    def report_total_discount(self, merchant: Merchant):
        total_discount = merchant.total_discount_given
        return total_discount

    def report_dues_for_user(self, user):
        return user.dues

    def report_users_at_credit_limit(self):
        user_list = []
        for user in self.user_dict.values():
            if user.residual_limit == 0:
                user_list.append(user.name)
        return user_list

    def report_total_dues(self):
        dues_list = []
        total = 0
        for user in self.user_dict.values():
            if user.dues != 0:
                total += user.dues
                dues_list.append((user.name, user.dues))
        dues_list.append(('total', total))
        return dues_list
