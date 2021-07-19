# find i for target >= ai

def binary_search(arr, target):
    start, end = -1, len(arr)
    while end-start > 1:
        partition = (start+end+1)//2
        print(start, end, partition)
        if arr[partition] == target: return partition
        if arr[partition] > target: end = partition
        else: start = partition
    return partition


if __name__ == "__main__":
    arr = [0,2,3,4,5,6,8,9,11,13,56,66,70]
    index = binary_search(arr,71)
    print(index)
    