from .find_min import find_min

def find_in_rotated(arr, target):
    offset = find_min(arr)
    print(offset)
    lo = 0
    hi = len(arr) - 1
    def get_offsetted(val): return val + offset - len(arr) if (val + offset) >= len(arr) else val + offset
    
    while lo <= hi:
        mid = lo + (hi-lo)//2
        mid_o = get_offsetted(mid)
        print(lo, hi, mid, mid_o, '>', arr[mid_o])
        if arr[mid_o] == target: 
            return mid_o
        if arr[mid_o] > target: hi = mid-1
        else: lo = mid+1
        
if __name__ == "__main__":
    # [0,0,1,2,2,2,3,4,5,6,7]
    arr = [3,4,5,6,7,0,0,1,2,2,2]
    # arr = [0,0,0,0,0]
    print(find_in_rotated(arr, 5))