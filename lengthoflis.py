class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i+1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        print(dp)
        for re in dp:
            res = max(res,re)
        return res


sol = Solution()
print(sol.lengthOfLIS([4,10,4,3,8,9]))