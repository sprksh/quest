def searchMatrix(matrix, target: int) -> bool:
    lo, hi = 0, len(matrix)*len(matrix[0])-1
    def get_val(i): return matrix[i//len(matrix[0])][i%len(matrix[0])]
    while lo <= hi:
        mid = lo + (hi-lo)//2
        print(lo, hi, mid)
        v = get_val(mid)
        if v == target: return True
        if v > target: hi = mid -1
        else: lo = mid + 1
    return False
    
if __name__ == "__main__":
    m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(searchMatrix(m, 61))