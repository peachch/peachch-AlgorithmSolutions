class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        def dp(nums,i,res):
            nonlocal result
            if i == len(nums):
                if res == 0:
                    return  1
                return  0
            key = str(i) + "," + str(res)
            # memo[key] = result
            if memo.get(str(i) + "," + str(res)):
                return memo[key]

            result = dp(nums,i+1,res-nums[i]) + dp(nums,i+1,res+nums[i])
            memo[key] = result
            return result

        memo = {}
        result = 0
        return dp(nums,0,target)

sol = Solution()
print(sol.findTargetSumWays([1,1,1,1,1],3))