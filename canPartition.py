class Solution:
    def canPartition(self, nums) -> bool:
        _sum = 0
        for i in nums:
            _sum += i
        if _sum%2 != 0:return False
        _sum = int(_sum/2)
        dp = [[False for _ in  range(_sum+1)] for _ in range(len(nums)+1)]
        print(dp)
        for i in range(len(dp)):
            dp[i][0] = True
        # 这里i要从1开始
        for n in range(1,len(nums)+1):
            for w in range(1,_sum+1):
                if w < nums[n-1]:
                    dp[n][w] = dp[n-1][w]
                else:
                    dp[n][w] = dp[n-1][w-nums[n-1]] | dp[n-1][w]
        return dp[len(nums)][_sum]

sol = Solution()
print(sol.canPartition([1,5,11,5]))