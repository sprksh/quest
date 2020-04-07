

def find_max_value(max_weight, weight_val_dict):
    max_weight_val_dict = {}

    def max_val_recr(remaining_weight):
        if remaining_weight == 0:
            return 0
        if remaining_weight in max_weight_val_dict:
            return max_weight_val_dict[remaining_weight]
        else:
            max_value = min([
                v + max_val_recr(remaining_weight-w) 
                for w, v in weight_val_dict.items()
                if remaining_weight >= w
            ])
            max_weight_val_dict[remaining_weight] = max_value
            return max_value

    max_value = max_val_recr(max_weight)
    print(max_weight_val_dict)
    return max_value



if __name__ == "__main__":
    values = [60,100,120]
    weights = [10,20,30]
    weight_val_dict = {weights[i]: values[i] for i in range(len(values))}
    max_weight = 50
    knapsack_value = find_max_value(max_weight, weight_val_dict)
    print(f"max knapsack value: {knapsack_value}")

