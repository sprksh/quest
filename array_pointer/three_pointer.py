"""
sort an array of 0, 1 & 2

[1,2,0,0,0,1,2,1,1,0,2]
 ^                   ^

while mid index < hi index:
    if mid == 0: swap with lo, move lo right till it is not 0
    if mid == 2: swap with hi, move hi left till it is not 2
if lo < mid: swap; move mid right

"""
def sort_arr012(arr):
    lo, mid, hi = 0, 0, len(arr)-1
    while mid <= hi:
        if arr[mid] == 0:
            arr[mid], arr[lo] = arr[lo], arr[mid]
            lo += 1; mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
        else: mid += 1
    print(arr)

def sort_arr01(arr):
    lo, hi = 0, len(arr)-1
    while lo < hi:
        if arr[lo]> arr[hi]:
            arr[lo], arr[hi] = arr[hi], arr[lo]
        if arr[lo] == 0: lo += 1
        if arr[hi] == 1: hi -= 1
    print(arr)
        

"""
arr1 = [1,2,5,7,9]
arr2 = [3,4,6,9]
sort into
[1,2,3,4,5], [6,7,8,9]
"""
def sort_two_arrays(arr1, arr2):
    pass




