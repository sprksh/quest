"""
stock_prices = [10, 22, 5, 75, 65, 80]
buyer can only purchase and have only 1 unit at a time

"""


def maximize_profit(stock_prices, k):
    max_profit_dict = {}
    psap = 0

    def max_profit_recur(reamining_days, reamining_k, psap):
        if not reamining_days or not reamining_k and not psap:
            return 0
        #  we can memoize results with (reamining_days, reamining_k, psap) as keys

        else:
            if psap:
                max_profit = max(
                    reamining_days[0] - psap + max_profit_recur(reamining_days[1:], reamining_k-1, 0), # sold,
                    max_profit_recur(reamining_days[1:], reamining_k, psap) # skip
                )
            else:
                max_profit = max(
                    max_profit_recur(reamining_days[1:], reamining_k, psap), # skip
                    max_profit_recur(reamining_days[1:], reamining_k, psap+reamining_days[0]) # purchase
                )
            return max_profit
    return max_profit_recur(stock_prices, k, psap)

if __name__ == "__main__":
    stock_prices, k = [10, 22, 5, 75, 65, 80], 2
    stock_prices, k = [12, 14, 17, 10, 14, 13, 12, 15], 3
    stock_prices, k = [100, 30, 15, 10, 8, 25, 80], 3
    max_profit = maximize_profit(stock_prices, k)
    print(max_profit)