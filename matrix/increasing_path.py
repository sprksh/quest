class Solution:
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        if not matrix or m==0 or n==0: return 0
        ans = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        mem = [[None for i in range(n)] for i in range(m)]
        
        def dfs(i, j):
            if mem[i][j]: return mem[i][j]
            cur_max = 0
            for d in directions:
                ii, jj = i+d[0], j+d[1]
                if 0<=ii<m and 0<=jj<n and matrix[ii][jj] < matrix[i][j]:
                    cur_max = max(cur_max, dfs(ii,jj))
            mem[i][j] = cur_max + 1
            return cur_max + 1
                    
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans
        
if __name__ == "__main__":
    matrix = [[3,4,5],[3,2,6],[2,2,1]]
    Solution().longestIncreasingPath(matrix)