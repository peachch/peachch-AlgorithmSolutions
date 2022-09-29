class Solution:
    def rob(self, nums) -> int:
        def dp(start,end):
            global ans
            if start >= end:return 0
            if (start,end) in memo:return memo[(start,end)]
            for i in range(start,end):
                ans = max(nums[start]+dp(start+2,end),dp(start+1,end))
            memo[(start,end)] = ans
            return ans
        memo = {}
        ans = 0
        n = len(nums)
        return max(dp(0,n-1),dp(1,n))

sol = Solution()
print(sol.rob([1,2,3]))