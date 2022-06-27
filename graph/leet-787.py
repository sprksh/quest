class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        from collections import defaultdict
        from functools import lru_cache
        graph = defaultdict(list)
        for frm,to,cost in flights:
            graph[frm].append((to, cost))
        
        cache = {}
        
        @lru_cache(None)
        def dfs(node, stops):
            if node == dst:
                return 0
            if stops < 0: return float('inf')
            ans = float('inf')
            for nxt, price in graph[node]:
                ans = min(ans, dfs(nxt, stops-1)+ price) 
            return ans
        
        result = dfs(src, k)
        
        return result if result != float('inf') else -1