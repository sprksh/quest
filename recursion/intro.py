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


def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


def path_sum(tree, root, val):
    count = 0
    s = 0
    def add_sum(tree, node, s, count):
        if not node.left and not node.right:
            if s == val:
                count += 1
            s = 0
        else:
            add_sum(tree, node.left, s, count)
            add_sum(tree, node.right, s, count)
    add_sum(tree, root, s, count)




def cut_rod():
    pass


def power_sum():
    pass