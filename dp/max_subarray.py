"""
Maximum subarray problem:

given an array, find subarray of max sum.

Below solution is kadane's algo.
But how is this solution dynamic programming?
"""

def find_max_subarray(arr):
    positive_sum_till_this_index = 0
    max_sum_overall = 0

    for i in arr:
        sum_till_this_index = positive_sum_till_this_index + i
        positive_sum_till_this_index = sum_till_this_index if sum_till_this_index >= 0 else 0
        if positive_sum_till_this_index > max_sum_overall:
            max_sum_overall = positive_sum_till_this_index
    
    return max_sum_overall


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    max_sum = find_max_subarray(arr)
    print(f"max sum: {max_sum}")