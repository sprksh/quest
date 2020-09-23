def binary_search(array, target, start_index=0, end_index=None, step=0):
    considered_array = array[start_index:end_index]
    print(considered_array)
    array_length = len(considered_array)
    mid_index = start_index + (array_length // 2)

    if array[mid_index] == target:
        print(mid_index)
        print(step)
        return

    if array_length == 0:
        print("Dafaq! Target not found in element")
        return

    if array[mid_index] > target:
        start_index, end_index = start_index, mid_index
    elif array[mid_index] < target:
        start_index, end_index = mid_index, end_index

    binary_search(array, target, start_index, end_index, step+1)
    return

if __name__ == "__main__":
    print(binary_search(list(range(15, 400)), 5))
