
'''
Given a 2D binary matrix filled with 0’s and 1’s, find the largest rectangle containing only 1’s and return its area.
Input :
[
[1,0,1,0,0],
[1,0,1,1,1], 
[1,1,1,1,1],
[1,0,0,1,0]
]

2 0 2 1 1 
3 1 3 2 2
4,0,0,3,0  
Output :
6

Input : 
[
[1,0,1,0,0], 1
[1,1,1,1,1], 5
[1 1,1,1,1], 5
[1,0,0,1,0]  1
]

1 0 1 0 0 - 1 
2 1 2 1 1 - 5
3 2 3 2 2 - 10
4 0 0 3 0 - 4 

Output:
10

Constrains :
Dimension of the matrix : m x n
0 <= m, n <= 1000

[[1, -1, 1, -1, -1], [1, -1, 2, 1, 1], [1, 1, 2, 1, 1], [1, -1, -1, 1, -1]]

[3, 1, 3,2,2] - 5,6

'''

arr = [
[1,0,1,0,0],
[1,0,1,1,1],
[1,1,1,1,1],
[1,0,0,1,0]
]

agg_arr = [[0]* len(arr[0]) for i in range(len(arr))]
m = len(arr)
n = len(arr[0])

def get_cumulation_from_above(i, j):
    agg_arr[i][j] = 1
    if m > i > 0:
        if agg_arr[i-1][j] > 0:
            agg_arr[i][j] = agg_arr[i-1][j] + 1
    
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            get_cumulation_from_above(i, j)

for i in agg_arr:
    print(i)
        
max_rectangle_area = 0


"""
2 0 2 1 1
3 1 3 2 2

4,0,0,3,0  
"""

def max_histogram(arr):
    max_area = 0
    for i in arr


for row in agg_arr:
    min_from_row = 1
    max_continuous = 0
    max_row_area = 0
    for i in row:
        if i > -1:
            min_from_row = min(min_from_row, i)
            max_continuous += 1
        else:
            max_continuous = 0
    area_row = min_from_row * max_continuous
    max_rectangle_area = max(max_rectangle_area, area_row)
    



print(max_rectangle_area)
print(agg_arr)

