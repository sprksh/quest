
# this one becomes O(n)
def findMinWithDuplicates(nums) -> int:
    lo, hi = 0, len(nums)-1
    while lo < hi:
        print(lo, hi)
        mid = lo + (hi-lo)//2
        if nums[mid] > nums[hi]: lo = mid +1
        elif nums[mid] == nums[hi]: hi = hi-1
        else: hi = mid 
    return nums[lo]


def find_min(arr):
    lo = 0
    hi = len(arr) -1
    while lo<hi:
        mid = lo + (hi-lo)//2
        if arr[lo] < arr[hi]: return lo
        if arr[mid] >= arr[lo]: lo = mid + 1
        else: hi = mid
    return lo
    
    
    
if __name__ == "__main__":
    # [0,0,1,2,2,2,3,4,5,6,7]
    arr = [3,4,5,6,7,0,0,1,2,2,2]
    # arr = [0,0,0,0,0]
    print(find_min(arr))
    # print(find_in_rotated(arr, 5))