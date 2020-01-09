# A very basic code to print a list in reverse using recursion


def print_reverse(l, i=0):
    "print an array in reverse using recursion"
    if i != len(l)-1:
        j =i+1
        print_reverse(l, j)
    print(l[i])


def num_sum(n):
    "sum of digits in number using recursion"
    r, q = n%10, n//10
    if q > 0:
        r += num_sum(q)
    return r


def pow(x, n):
    "nth power of x in log(n) steps using recursion"
    if n == 0:
        return 1
    u = pow(x, n//2)
    if n%2 == 1:
        return x * u*u
    else:
        return u*u


def tower_of_hanoi(l):

    class Ring:
        def __init__(self, size, tower):


    first = l.copy()
    intermediate = []
    final = []
    d = {_: first for _ in l}
    for i in l:
        pass



    if not intermediate or intermediate[-1] < i:
        intermediate.append(i)



def cut_rod():
    pass


def power_sum():
    pass