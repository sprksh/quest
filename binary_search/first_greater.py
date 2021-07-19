def first_greater(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + (hi-lo)//2
        if arr[mid] <= target: lo = mid+1
        else: hi = mid
    return hi if hi<len(arr) else -1


if __name__ == "__main__":
    arr = [0,1,5,7,8,10,12,15]
    print(first_greater(arr, 2))