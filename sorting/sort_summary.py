from heap.heapify import Heap
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
        pass

    @timer()
    def merge_sort(self, array):
        if not array:
            array = self.array

        print("Merge Sort: %s" % str(array))

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

        if len(self.array) > 1:
            x = len(self.array) // 2
            left_array = self.array[:x]
            right_array = self.array[x:]
            self.merge_sort(left_array)
            self.merge_sort(right_array)

            return merge(array, left_array, right_array)


if __name__ == "__main__":
    count = 100
    import random
    array = [random.randint(0, count) for _ in range(count)]

    Sort(array[:]).heap_sort()
    Sort(array[:]).heap_sort_internal()
    Sort(array[:]).merge_sort()
