def get_combinations(arr, r):
    combinations = []
    def combine(arr, i, current=[]):
        if len(current) == r:
            combinations.append(current)
            return
        if i == len(arr):
            return
        combine(arr, i+1, current + [arr[i]])
        combine(arr, i+1, current)
    combine(arr, 0)
    return combinations


if __name__ == "__main__":
    arr = [1,2,3, 4]
    print(get_combinations(arr, 2))