"""
[
        0,1,2,3
    0, [0,1,*,*],
    1, [1,0,0,0],
    2, [1,0,0,0],
    3, [1,0,0,0],
]

Algo:
initially prepare a adjacency matrix only with connected ones, keepeng rest as inf
for k in range(n):
    A(k)[i,j] = min(A(k-1)[i,j], A(k-1)[i,k]+A(k-1)[k,j])
"""

# n^3 solution for leetcode 834

from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        answer = []
        mat = [[0 if i == j else float('inf') for i in range(n)] for j in range(n)]
        for [i,j] in edges:
            mat[i][j] = 1
            mat[j][i] = 1
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        
        return [sum(x) for x in mat]

