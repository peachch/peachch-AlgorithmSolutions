class Solution:
    def maxProfit(self, prices) -> int:
        dp = [[0,float("-inf")] for _ in range(len(prices))]
        print(dp)
        for i in range(len(prices)):
            # if i-1 == -1:
            #     dp[i][0] = 0
            #     dp[i][1] = -prices[i]
            #     continue
            # print(dp[-1][0])
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][0]-prices[i],dp[i-1][1])
        print(dp)
        return dp[len(prices)-1][0]


sol = Solution()
print(
    sol.maxProfit([7,1,5,3,6,4])
)