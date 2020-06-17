def find_max_sum(arr, k):
    # complexity: n*k
    max_sum = 0
    for ref in range(len(arr) - k + 1):
        summation = 0
        for slider in range(k):
            summation  += arr[ref+slider]
        max_sum = summation if summation > max_sum else max_sum
    return max_sum


def find_max_optimized(arr, k):
    # complexity: n
    max_sum = 0
    sliding_sum = 0
    for i in range(len(arr)):
        if i < k:
            sliding_sum += arr[i]
        else:
            sliding_sum = sliding_sum+ arr[i] - arr[i-k]
        if i >= k-1:
            max_sum = sliding_sum if sliding_sum > max_sum else max_sum
    return max_sum


def test_find_max_sum():
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 8]
    k = 3
    print("1: ", find_max_optimized(arr, k))
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k = 9
    print("2: ", find_max_optimized(arr, k))
    arr = [1, 2, 3, 1, -4, 5, 2, 3, 6]
    k = 3
    print("3: ", find_max_optimized(arr, k))



def longest_substring(string, k):
    """longest substring with k uniques"""
    longest_substring_length_with_k_uniques = 0
    char_dict = {}
    start_index = 0
    remove_index = 0
    
    def add_char(x):
        nonlocal char_dict
        char_dict[x] = char_dict.setdefault(x, 0) + 1
    
    def remove_char(x):
        nonlocal char_dict, remove_index
        char_dict[x] = char_dict[x] - 1
        if char_dict[x] == 0:
            char_dict.pop(x)
        remove_index = remove_index + 1
    
    def check_condition():
        nonlocal char_dict, start_index, longest_substring_length_with_k_uniques
        if len(char_dict) == k:
            substring_length_with_k_uniques = sum(char_dict.values())
            if substring_length_with_k_uniques > longest_substring_length_with_k_uniques:
                longest_substring_length_with_k_uniques = substring_length_with_k_uniques
                start_index = remove_index
        if len(char_dict) > k:
            remove_char(string[remove_index])
            check_condition()

    for x in string:
        add_char(x)
        check_condition()
    print(start_index, longest_substring_length_with_k_uniques)
    return string[start_index: start_index + longest_substring_length_with_k_uniques]


def test_longest_substring():
    s, k = "aabbcc", 1
    print(longest_substring(s, k))
    s, k = "aabbcc", 2
    print(longest_substring(s, k))
    s, k = "aabbcc", 3
    print(longest_substring(s, k))
    s, k = "wwwallahhh", 3
    print(longest_substring(s, k))
    s, k = "aabacbebebe", 3
    print(longest_substring(s, k))



if __name__ == "__main__":
    # test_find_max_sum()
    test_longest_substring()
