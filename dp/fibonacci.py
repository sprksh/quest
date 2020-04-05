"""
fib(n) = fib(n-1) + fib(n-2)
fib(0) = 1
fib(1) = 1
"""

# memoization:

def fib_m(n):
    m_dict = {}
    for i in range(n+1):
        if i == 0:
            x = 0
        elif i == 1:
            x = 1
        else:
            x = m_dict[i-1] + m_dict[i-2]
        m_dict[i] = x
    return m_dict[n]

# a bottom up approach: easy

if __name__ == "__main__":
    print(fib_m(100))
