def find_min_coin_for(x, supply):
    min_coin_dict = {}


    def find_min_recr(remaining_val):
        if remaining_val == 0:
            return 0
        if remaining_val in min_coin_dict:
            return min_coin_dict[remaining_val]
        else:
            print(remaining_val)
            all_combinations = [
                1 + find_min_recr(remaining_val-c) 
                for c in supply 
                if c <= remaining_val
            ]
            min_comb = min(all_combinations)
            min_coin_dict[remaining_val] = min_comb
            return min_comb
    
    min_coins = find_min_recr(x)
    return min_coin_dict[x]

if __name__ == "__main__":
    supply = [9,6,5,1]
    min_coins = find_min_coin_for(11, supply)
    print(f"min coins{min_coins}")
