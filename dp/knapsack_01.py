
"""
1. if no remaining weight: return 0
2. take decision whether to include or exclude current entry
"""

def solve_knapsack(profits, weights, capacity):
    max_profit_cache = {}
    def knapsack_recursive(profits, weights, capacity, currentIndex):
        if capacity <= 0 or currentIndex >= len(profits): return 0
        if currentIndex in max_profit_cache: return max_profit_cache[currentIndex]
        # profit1 = 0
        if weights[currentIndex] <= capacity:
            profit1 = profits[currentIndex] + knapsack_recursive(profits, weights, capacity - weights[currentIndex], currentIndex + 1)
        profit2 = knapsack_recursive(profits, weights, capacity, currentIndex + 1)
        max_profit_cache[currentIndex] = max(profit1, profit2)
        print(max_profit_cache)
        return max_profit_cache[currentIndex]
    return knapsack_recursive(profits, weights, capacity, 0)


if __name__ == "__main__":
    values = [20, 5, 10, 40, 15, 25]
    weights = [1, 2, 3, 8, 7, 4]
    max_weight = 10
    knapsack_value = solve_knapsack(values, weights, max_weight)
    print(f"max knapsack value: {knapsack_value}")

