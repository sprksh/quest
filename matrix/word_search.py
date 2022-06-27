class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def recr(i, j, suffix):
            if len(suffix) == 0: 
                return True
            if i <0 or j<0 or i == m or j ==n or board[i][j] != suffix[0]: return False
            
            ret = False
            board[i][j] = '#'
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ret = recr(i+x, j+y, suffix[1:])
                if ret: break
            board[i][j] = suffix[0]
            return ret
        
        for i in range(m):
            for j in range(n):
                if recr(i, j, word):
                    return True
        return False
                
# why this is wrong      
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recr(i, j, path):
            if len(path) == len(word): return True
            if len(path) >= len(word): return False
            
            dirs = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            
            for x,y in dirs:
                if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]): continue
                if len(path) < len(word) and board[x][y] != word[len(path)]: continue
                if (x,y) in path: continue
                path.append((x,y))
                x = recr(x, y, path)
                path.pop()
                return x
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if recr(i, j, [(i,j)] ):
                        return True
        return False    
            
            