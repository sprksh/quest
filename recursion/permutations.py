def get_permutations(arr, r):
    permutations = []
    def permute(arr, index, current=[]):
        if index == r:
            permutations.append(current.copy())
            return
        for i in range(index, len(arr)):
            current.append(arr[i])
            arr[i], arr[index] = arr[index], arr[i]
            permute(arr, index+1, current)
            arr[i], arr[index] = arr[index], arr[i]
            current.pop()
    permute(arr, 0)
    return permutations

if __name__ == "__main__":
    arr = [1,2,3, 4]
    print(get_permutations(arr, 2))