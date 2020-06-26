"""
Its the coolest data structure

array rep:
i starts with 1
left child: 2i, right child: 2i+1
parent |i/2|

for index 0 : 
    l = 2i+1, r = 2i+2
    parent: 

inserting and deleting are log(n) operation
heapify is O(n) operation
"""


def heapify(arr, n, i):
    largest = i
    l, r = 2*i+1, 2*i+2
    
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr, n):
    for i in range(n//2 -1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr

def test_heap_sort():
    print(heap_sort([10,2,30,4,50,6,7, 11, 27], 9))

if __name__ == "__main__":
    test_heap_sort()



    

