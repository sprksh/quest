def print_spiral(mat):
    m, n = len(mat), len(mat[0])
    up, down, right, left = 0, m-1, n-1, 0
    while 