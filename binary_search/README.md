Getting binary search right is difficult.

https://zhu45.org/posts/2018/Jan/12/how-to-write-binary-search-correctly/

http://coldattic.info/post/95/

https://stackoverflow.com/questions/504335/what-are-the-pitfalls-in-implementing-binary-search

https://stackoverflow.com/questions/26564658/binary-search-and-invariant-relation


termination condition in while loop:

ensuring loop termination is bit tricky. Here is an overview:

while lo <= hi:
    mid = lo + (hi-lo)//2
    hi = mid - 1
    lo = mid + 1

this one is simple as size is decreasing in every loop for sure.

while lo < hi:
    mid = lo + (hi-lo)//2
    lo = mid + 1
    hi = mid

this will work because array will be shortened when (hi-lo) = 1 >>> lo + (hi-lo)//2 = lo >>> means either lo = lo+1 or hi = lo
in both case it will terminate.
It wouldn't have terminated if we had used while lo <= hi

One point to note here is we are depending upon the bias of lo + (hi-lo)//2 towards lo.


while lo < hi:
    mid = lo + (hi-lo)//2
    hi = mid - 1
    lo = mid

This will not terminate when hi = lo+1. So we will have to change mid calculation to 

while lo < hi:
    mid = hi - (hi-lo)//2
    hi = mid - 1
    lo = mid

This will work because 
