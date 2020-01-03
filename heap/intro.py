"""
First, heap is a data structure as well as the runtime allocation of memory on RAM.
Do these two have any relation? no.
https://stackoverflow.com/questions/1699057/why-are-two-different-concepts-both-called-heap

Do first let's talk about heap memory.

What is heap and stack in memory management
https://www.youtube.com/watch?v=_8-ht2AKyH4

How memory is managed in python
https://www.youtube.com/watch?v=arxWaw-E8QQ

In python objects are stored in heap whereas pointers are stored in stack


Heap Data Structure:
Intro to heap: https://www.youtube.com/watch?v=HqPJF2L5h9U

when taking out the element from from heap, you only take out the top element
(thats the concept of a heap. thats why it is used as a priority queue)

Heap sort:
data is arranged in heap and we keep on deleting the top-most entry out of it and storing in a list
at the end, that gives us a sorted list.

Time taken to create a heap from list of numbers: nlogn
Time taken to remove each element from hep to put in a list: logn >> n element nlogn
So total time: O(nlogn)

Heapify:
Heapify can only be applied to a node only if children nodes are heapified
The process of converting complete binary tree into a heap.
The heap is made upwards from bottom
Heapify is O(n)
https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity


"""


class Heap:
    """
    Heap will be an array where we do the 2i +1, 2i + 2 for finding the left & right
    children of a node.

    """
    def __init__(self):
        self.heap_array = []

    def heap_sort(self):
        pass

    def heapify(self, arr, n, i):
        pass

    def insert_in_heap(self):
        pass

    def delete_from_heap(self):
        pass

    def priority_queue(self):
        pass
