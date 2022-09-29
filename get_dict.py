class Solution:
    def twoSum(self, nums, target: int):
        # count = collections.Counter(nums)
        index_dict = {}
        for i in range(len(nums)):
            index_dict[nums[i]] = i
        for i in range(len(nums)):
            new_t = target - nums[i]
            if index_dict.get(new_t) and index_dict[new_t] != i:
                return [i, index_dict[new_t]]


sol = Solution()
print(sol.twoSum(
    [3,3,6],9
))