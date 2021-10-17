# k - way merge
'''
1. merge k sorted arrays >> use k min heap > push smallest from each array into the heap and get the min > track the array 
    from which the popped entry was and push the next entry from that into heap > continue till the end >
    Time complexiy : nk log(k)
2. merge k unsorted array >> if you use heap >> Time Complexity: nknklog(k). while directly concatenate and sort > nklog(nk)



sliding window max

kth max element in stream

'''