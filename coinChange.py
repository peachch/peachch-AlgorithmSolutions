class Solution:
    def coinChange(self, coins, amount: int) -> int:
        memory = dict()
        def dp(n):
            if n in memory:return memory[n]
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('INF')
            for i in coins:
                sub = dp(n - i)
                if sub == -1:continue
                res = min(res,sub+1)
            memory[n] = res if res != 'INF' else -1
            return memory[n]
        return dp(amount)


sol = Solution()
print(sol.coinChange([1,2],3))