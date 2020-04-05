"""
Length array
cost array
rod length

all posible ways of cutting and associated cost
maximum cost is one thing.
the exact cuts to achieve maximum cost is also required

optimal substructure: basically string start

"""

def cut_the_rod(rod_length, cost_array, length_array):
    remaining_length = rod_length

    total_cost = 0

    def get_max_cost(remaining_length):
        for i in length_array:
            cut = i
            remaining_length -= cut
            if remaining_length <= 0:
                return
            else:
                get_max_cost(remaining_length)

        
        
