from pay_later import PayLaterService


class InputHandler:

    @staticmethod
    def handle_input(pay_later_service: PayLaterService, input_string):
        input_data = input_string.split(' ')
        command, details = input_data[0], input_data[1:]

        if command == "report":
            if details[0] == "total-dues":
                return pay_later_service.report_total_dues()
            if details[0] == "users-at-credit-limit":
                return pay_later_service.report_users_at_credit_limit()
            if details[0] == "discount":
                merchant = pay_later_service.get_merchant_by_name(details[1])
                return pay_later_service.report_total_discount(merchant)
            if details[0] == "":
                user = pay_later_service.get_user_by_name(details[1])
                return pay_later_service.report_dues_for_user(user)

        if command == "new":
            if details[0] == "user":
                return pay_later_service.register_user(details[1], details[2], float(details[3]))
            if details[0] == "merchant":
                return pay_later_service.register_merchant(details[1], details[2], float(details[3]))
            if details[0] == "txn":
                user = pay_later_service.get_user_by_name(details[1])
                merchant = pay_later_service.get_merchant_by_name(details[2])
                return pay_later_service.handle_transaction(user, merchant, float(details[3]))

        if command == "payback":
            user = pay_later_service.get_user_by_name(details[0])
            amount = float(details[1])
            return pay_later_service.handle_payback(user, amount)


if __name__ == "__main__":
    pay_later_service = PayLaterService()
    while True:
        input_string = input("> ")
        if input_string == 'debug':
            import ipdb; ipdb.set_trace()
        result = InputHandler.handle_input(pay_later_service, input_string)
        print(result)
