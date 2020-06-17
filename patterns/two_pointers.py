def sorted_squares(arr):
    n = len(arr) - 1
    for i in range(len(arr)):
        if abs(arr[i]) < abs(arr[n - i]):
            arr[i]



def check_two_element_sum(arr, s):
    n = len(arr)
    i, j = 0, n-1
    while i<j:
        if arr[i] + arr[j] > s:
            j -= 1
        elif arr[i] + arr[j] < s:
            i +=1
        else:
            print(i, j, arr[i], arr[j])
            return True
    return False

def test_check_two_element_sum():
    arr, s = [1,3,4,5,6,7], 7
    print(check_two_element_sum(arr, s))
    arr, s = [1,3,4,5,6,7], 11
    print(check_two_element_sum(arr, s))
    arr, s = [1,3,4,5,6,7], 16
    print(check_two_element_sum(arr, s))


def all_triplets_with_zero_sum(arr):
    triplets = []
    arr.sort()
    n = len(arr)
    for i in range(n):
        x = arr[i]
        l, r = i+1 , n-1
        while l < r:
            if x + arr[l] + arr[r] == 0:
                print((x, arr[l], arr[r]))
                triplets.append((x, arr[l], arr[r]))
                l+=1
            elif x + arr[l] + arr[r] > 0:
                r -=1
            else:
                l += 1
    return triplets

    
def test_all_triplets_with_zero_sum():
    print(all_triplets_with_zero_sum([0, -1, 2, -3, 1]))



if __name__ == "__main__":
    # test_check_two_element_sum()
    test_all_triplets_with_zero_sum()
