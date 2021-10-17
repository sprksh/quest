class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [0]+ [float('inf')]*amount
        
        for i in range(1,amount+1):
            dp[i] = min([dp[i-c] if i>=c else float('inf') for c in coins]) + 1
            
        return dp[i] if not dp[i] == float('inf') else -1
        
        

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [0]* (amount+1)
        for i in range(1,amount+1):
            for c in coins:
                if c==i: dp[i] = 1
                if c < i:
                    dp[i]= dp[i-c] + 1 if dp[i-c] > 0 else 0
        return dp[-1] if dp[-1] else -1
        

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [0]+ [float('inf')]*amount
        
        for i in range(1,amount+1):
            for c in coins:
                if i ==c: dp[i]=1
                if i > c:
                    dp[i] = min(dp[i], dp[i-c] +1)
        return dp[i] if not dp[i] == float('inf') else -1