"""
crux is: you need to keep indexes of 'good' candidates in dek

dek:    a dek of 'good' indexes in current window, max length = k
        leftmost is index of sliding window max
algo:
    for i in range(len(nums)):
        remove all indexes of lower values than current from end of dek
        append current index at end of dek
        remove first index if it is out of the current window
        if i >= k: add sliding window max (val at leftmost index) to output
"""

def sliding_window_max(nums, k):
    from collections import deque
    output = []
    dek = deque(maxlen=k)
    
    for i, n in enumerate(nums):
        while dek and nums[dek[-1]] < n:
            dek.pop()
        dek.append(i)
        if i - dek[0] >= k:
            dek.popleft()
        if i >= k-1:
            output.append(nums[dek[0]])
    return output

def sliding_window_min(nums, k):
    from collections import deque
    output = []
    dek = deque(maxlen=k)
    
    for i, n in enumerate(nums):
        while dek and nums[dek[-1]] > n:
            dek.pop()
        dek.append(i)
        if i - dek[0] >= k:
            dek.popleft()
        if i >= k-1:
            output.append(nums[dek[0]])
    return output