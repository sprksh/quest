# gets first index of given number
def bisect_left(arr, target):
    lo, hi = 0, len(arr)-1
    while lo < hi:
        mid = lo + (hi-lo)//2
        if arr[mid] >= target: hi = mid 
        else: lo = mid + 1
    return lo if arr[lo] == target else -1


# gets last index of given number
def bisect_right(arr, target):
    lo,hi = 0, len(arr)-1
    while lo < hi:
        # used this hi-half strategy to get rid of loop termination issue
        mid = hi - (hi-lo)//2
        if arr[mid] <= target: lo = mid 
        else: hi = mid-1
    return lo if arr[lo] == target else -1
    

if __name__ == "__main__":
    arr = [0,0,1,5,7,7,8,10,12,15]
    # arr = [1,1,1]
    print(bisect_left(arr, 7))
    print(bisect_right(arr, 7))