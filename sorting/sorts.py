def quick_sort(arr):
    def partition(arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than the pivot
            if arr[j] < pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def quickSort(arr, low, high):
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            quickSort(arr, low, pi - 1)
            quickSort(arr, pi + 1, high)
        return arr

    _sorted = quickSort(arr, 0, len(arr) - 1)
    return _sorted


if __name__ == "__main__":
    _sorted = quick_sort([31,4,5,16,7,8,13,3,4,23,12,21])
    print(_sorted)
