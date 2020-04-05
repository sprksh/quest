
class KnapSack:
    @staticmethod
    def max_val(weights, values, cap):
        combined_arr = [[values[i], weights[i], values[i] / weights[i]] for i in range(len(values))]
        combined_arr_sorted = sorted(combined_arr, key=lambda x: x[-1], reverse=True)
        sack = []
        while cap > 0:
            entry = combined_arr_sorted[0]
            wt = entry[1]
            val = entry[0]
            if cap >= wt:
                sack.append(val)
                cap = cap - wt
                combined_arr_sorted.pop(0)
            else:
                val = cap * (val/wt)
                sack.append(val)
                cap = cap - val

        return sack


if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 50

    maxValue = KnapSack.max_val(wt, val, capacity)
    print("Maximum value in Knapsack =", sum(maxValue))