class Solution:
    def canPartition(self, nums) -> bool:
        _sum = 0
        for i in nums:
            _sum += i
        if _sum%2 != 0:return False
        _sum = int(_sum/2)
        dp = [False  for _ in range(_sum+1)]
        print(dp)
        dp[0] = True

        for n in range(1,len(nums)+1):
            w = _sum
            while w >= 0:
                if w-nums[n-1] >= 0:
                    dp[w] = dp[w-nums[n-1]] | dp[w]
                w-=1
        return dp[_sum]

sol = Solution()
print(sol.canPartition([1,5,11,5]))