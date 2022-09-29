class Solution:
    def removeDuplicates(self, nums) -> int:
        slow = fast = 0
        # res = [nums[0]]
        while fast < len(nums) - 1:
            fast += 1
            if nums[fast] != nums[slow]:
                # continue
                slow += 1
                nums[slow] = nums[fast]
        print(nums)
        return nums[:slow+1]

sol = Solution()
print(sol.removeDuplicates([1,1,2]))