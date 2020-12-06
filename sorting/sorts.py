def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
        return array
    return _quicksort(array, begin, end)

if __name__ == "__main__":
    arr = [13,4,5,16,7,8,31,3,4,23,12,21]
    _sorted = quicksort(arr, end=len(arr)-1)
    print(_sorted)
