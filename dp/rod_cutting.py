"""
Length array
cost array
rod length

all posible ways of cutting and associated cost
maximum cost is one thing.
the exact cuts to achieve maximum cost is also required

optimal substructure: basically string start

"""


def maximize_cost(rod_length, length_cost_dict):
    max_cost_length_dict = {}

    def max_cost(remaining_length):
        if remaining_length == 0:
            return 0
        if remaining_length in max_cost_length_dict:
            return max_cost_length_dict[remaining_length]
        else:
            print(remaining_length)
            all_costs = [
                ci + max_cost(remaining_length-li)
                for li, ci in length_cost_dict.items()
                if li <= remaining_length
            ]
            print(all_costs)
            maximum_cost = max(all_costs)
            max_cost_length_dict[remaining_length] = maximum_cost
            return maximum_cost
    
    maxi = max_cost(rod_length)
    print(maxi)
    print(max_cost_length_dict)
    return max_cost_length_dict[rod_length]


if __name__ == "__main__":
    rod_length = 56
    lengths = [1, 2, 3, 4, 5, 6, 7, 8]
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    length_cost_dict = {lengths[i]: prices[i] for i in range(len(lengths))}
    print(length_cost_dict)
    maxo = maximize_cost(rod_length, length_cost_dict)
    print(maxo)
