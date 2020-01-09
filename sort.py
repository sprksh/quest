from heap.heapify import Heap
from sorting.sorts import quick_sort
from utils import timer


class Sort:
    def __init__(self, array):
        self.array = array

    @timer()
    def heap_sort(self):
        _sorted = Heap(self.array).heap_sort()
        return _sorted

    @timer()
    def heap_sort_internal(self):
        _sorted = Heap(self.array).heap_sort_internal()
        return _sorted

    @timer()
    def bubble_sort(self):
        pass

    @timer()
    def quick_sort(self):
        arr = self.array
        quick_sort(arr)

    @timer()
    def merge_sort_sort(self):
        def merge_sort(array=None):
            def merge(array, left_array, right_array):
                i = j = k = 0
                while i < len(left_array) and j < len(right_array):
                    if left_array[i] < right_array[j]:
                        array[k] = left_array[i]
                        i += 1
                    else:
                        array[k] = right_array[j]
                        j += 1
                    k += 1

                # Checking if any element was left
                while i < len(left_array):
                    array[k] = left_array[i]
                    i += 1
                    k += 1

                while j < len(right_array):
                    array[k] = right_array[j]
                    j += 1
                    k += 1
                return array

            if len(array) > 1:
                x = len(array) // 2
                left_array = array[:x]
                right_array = array[x:]
                merge_sort(left_array)
                merge_sort(right_array)

                return merge(array, left_array, right_array)

        _sorted = merge_sort(self.array)
        return _sorted


if __name__ == "__main__":
    count = 1000
    import random

    array1 = [random.randint(0, count) for _ in range(count)]
    array2 = [random.randint(0, count) for _ in range(count)]
    array3 = [random.randint(0, count) for _ in range(count)]
    array4 = [random.randint(0, count) for _ in range(count)]

    Sort(array1).heap_sort()
    Sort(array2).heap_sort_internal()
    Sort(array3).merge_sort_sort()
    Sort(array4).quick_sort()

    """
    Here, we find that quick sort is the fastest of all although worst case performance of quicksort is o(n**2)
    """
