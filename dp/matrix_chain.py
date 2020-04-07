"""
Given a chain of matrix, find out the most optimal way to multiply them

m is rows, n is columns

clumns of A and Rows of B must be the same: n1 = m2
and resultant matrix = m1xn2
and number of operations = m1*n2

A = m1xn1
B = m2xn2

for optimal multiplication
m1*n2 should be minimum

Its a substring problem: eric demain: E:21, 12:00
"""


def optimize(matrix_list):
    l = len(matrix_list)
    cost_dict = {}

    def min_cost(i, j):
        print(i, j)
        if (i, j) in cost_dict:
            return cost_dict[(i, j)]
        if j == i+1:
            cost = matrix_list[i][0] * matrix_list[j][0] * matrix_list[j][1]
            cost_dict[(i,j)] = cost
            return cost
        if i >= j:
            return 0

        all_costs = [
            min_cost(i, k) + min_cost(k+1, j) + (
                    matrix_list[i][0]*matrix_list[k+1][0]*matrix_list[j][1]
            ) for k in range(i+1, j)
            # struggled for a bit in creating this equation with indices.
        ]
        print(all_costs)
        mc = min(all_costs)
        index = all_costs.index(mc)
        print(index)
        cost_dict[(i, j)] = mc
        return mc
    
    minimum_cost = min_cost(0, l-1)
    
    return minimum_cost


# gfg approach

import sys 
  
# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n 
def MatrixChainOrder(p, n): 
    # For simplicity of the program, one extra row and one 
    # extra column are allocated in m[][].  0th row and 0th 
    # column of m[][] are not used 
    m = [[0 for x in range(n)] for x in range(n)] 
  
    # m[i,j] = Minimum number of scalar multiplications needed 
    # to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where 
    # dimension of A[i] is p[i-1] x p[i] 
  
    # cost is zero when multiplying one matrix. 
    for i in range(1, n): 
        m[i][i] = 0
  
    # L is chain length. 
    for L in range(2, n): 
        for i in range(1, n-L+1): 
            j = i+L-1
            m[i][j] = sys.maxint 
            for k in range(i, j): 
  
                # q = cost/scalar multiplications 
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j] 
                if q < m[i][j]: 
                    m[i][j] = q 
  
    return m[1][n-1] 

if __name__ == "__main__":
    l = [10, 20, 30, 40, 30]
    haha = []
    for i in range(len(l)-1):
        haha.append((l[i], l[i+1]))
    print(list(haha))
    o = optimize(haha)
    print(o)
