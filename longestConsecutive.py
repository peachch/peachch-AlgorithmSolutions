class Solution:
    def longestConsecutive(self, nums) -> int:
        nums = sorted(nums)
        print(nums)
        lo = 0
        hi = 1
        res = 0
        while hi < len(nums):
            while hi < len(nums) and nums[hi - 1] == nums[hi] - 1:
                hi += 1
            print(hi, lo)
            res = max(res, hi - lo)
            lo = hi
            hi += 1
        return res

sol=Solution()
print(sol.longestConsecutive([0, 0, 1, 2, 3, 4, 5, 6, 7, 8]))