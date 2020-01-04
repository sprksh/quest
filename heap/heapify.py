# Much help taken from Mohit Kumra's code on geeksforgeek


class Heap:
    """
    Heap will be an array where we do the 2i +1, 2i + 2 for finding the left & right
    children of a node.

    """
    def __init__(self, array):
        self.array = array
        # array representation of heap in list: 2i+1, 2i+2 wala concept
        self.array_len = len(self.array)
        self.heapify_count = 0

    def build_a_max_heap(self):

        for i in range(self.array_len, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        # for sorting an array, you need to heapify it and take out the first
        # element and keep repeating the same till the last element.

        # build a max heap
        self.build_a_max_heap()
        print("Max Heap array: %s" % str(self.array))

        # extract first element recursively
        for i in range(self.array_len - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]  # swap
            self.max_heapify(i=0, till=i)
            # print(self.array)

        return self.array

    def max_heapify(self, i=0, till=None):
        self.heapify_count += 1
        # calls itself recursively to heapify subtree with root at i
        # it should be able to heapify a subtree in a heap at index i
        # please note that a heapified array is not sorted
        # one thing that heapify ensures is that the top element is
        # the greatest or the smallest but only within that subtree
        if not till:
            # n is the level till which the list needs to be heapified
            till = self.array_len

        print("heapifying at  index %s" % i)

        largest_in_subtree_index = i
        left_child_index, right_child_index = 2*i+1, 2*i+2
        if till > left_child_index and self.array[left_child_index] > self.array[i]:
            largest_in_subtree_index = left_child_index
        if till > right_child_index and self.array[right_child_index] > self.array[largest_in_subtree_index]:
            largest_in_subtree_index = right_child_index

        if largest_in_subtree_index != i:
            self.array[i], self.array[largest_in_subtree_index] = self.array[largest_in_subtree_index], self.array[i]
            self.max_heapify(largest_in_subtree_index, till)

    def insert_in_heap(self):
        # insert at end
        # heapify at root? or heapify recursively from bottom?
        pass

    def delete_from_heap(self):
        # remove root
        # move last element to root
        # run heapify at root
        pass

    def priority_queue(self):
        pass

    def heap_sort_internal(self):
        from heapq import heappop, heappush
        heap = []
        for element in self.array:
            heappush(heap, element)

        ordered = []

        # While we have elements left in the heap
        while heap:
            ordered.append(heappop(heap))

        return ordered


if __name__ == "__main__":
    count = 100
    import random
    array = [random.randint(0, count) for i in range(count)]
    # array = list(range(count, -1, -1))
    h = Heap(array)
    sorted_array = h.heap_sort()
    print("Sorted array is %s" % str(sorted_array))
    print("Sorted in %s heapify calls" % h.heapify_count)

    """
    Here, note that heapify is an O(1) operation for leaf node that is n/2 of entries and h <~ log(n)
    for other entries based on their height in the tree and which are executed by recursive heapify calls log(n) times 
    The count that we are seeing here takes care of the recursive calls also.
    Here, for 1 lakh (1,00,000) count:
        heapify calls ~ 16,74,739
    for count 10,000 == 100**2:
        heapify calls ~ 134232
        
    for a reverse sorted array of 100: heapify calls is 618
    for a random array of 100, heapify calls ~ 670
    # sorting a totally unsorted array is easier?
    """
