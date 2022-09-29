class Solution:
    def jump(self, nums) -> int:
        i = 0
        end = 0
        farest = 0
        jump = 0
        for i in range(len(nums)-1):
            farest = max(farest,nums[i] + i)
            if i == end:
                jump += 1
                end = farest
        return jump


sol = Solution()
print(sol.jump([2,3,1,1,4]))