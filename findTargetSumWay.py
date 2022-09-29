class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        def trackback(sum,i):
            # 这里要分开if，因为无论有没有找到res，只要i遍历完了，就需要return
            if i == len(nums):
                nonlocal res
                if sum == target:
                    res += 1
                return res
            for opt in [1,-1]:
                sum += nums[i] * opt
                trackback(sum,i+1)
                sum -= nums[i] * opt
            #
            # sum -= nums[i]
            # trackback(sum,i+1)
            # sum += nums[i]

        res = 0
        trackback(0,0)
        return res

sol = Solution()
print(sol.findTargetSumWays([1,1,1,1,1],3))