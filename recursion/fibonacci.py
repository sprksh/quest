def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)




def fib(n):
    arr = [-1 for i in range(n+1)]

    def fibo(n):
        if n == 0 or n == 1:
            return 1
        if arr[n] != -1:
            return arr[n]
        else:
            f1 = fibo(n-1)
            f2 = fibo(n-2)
            f = f1 + f2
            arr[n] = f
            return f
    f = fibo(n)
    return f


def merge_sort(arr):
    def merge(arr, L, R):
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
        return arr

    if len(arr) > 1:
        x = len(arr) // 2
        L = arr[:x]
        R = arr[x:]
        merge_sort(L)
        merge_sort(R)

        return merge(arr, L, R)


