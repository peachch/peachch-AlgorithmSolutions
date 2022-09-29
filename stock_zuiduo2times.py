class Solution:
    def maxProfit(self, prices) -> int:
        # 三维数组的意思是 第一维是后面两维的个数
        # dp[n][k+1][s]
        dp = [[[_ for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]

        for i in range(len(prices)):
            # k应该定义在这里，这样会遍历i的所有情况下，从2开始递减的k
            # 等同于 for int k=2;k>=1;k--
            k = 2
            while k >=1:
                # 这个模块处理的是i-1=-1时的base case，也就是要遍历所有i和k的情况
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    # 这里k需要被全部遍历，这里continue之后会调到k>=1处，所以需要对k做自减
                    k -= 1
                    # 将这里的i和k全部遍历完
                    continue
                # 这里约定k在买入时候－1，则在卖出时就不变
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
                dp[i][k][1] = max(dp[i-1][k-1][0]-prices[i],dp[i-1][k][1])
                k = k-1
        print(dp)
        return dp[len(prices)-1][2][0]


sol = Solution()
print(
    sol.maxProfit([3,3,5,0,0,3,1,4])
)