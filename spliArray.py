class Solution:
    def splitArray(self, nums, m: int) -> int:
        def split(_max, nums):
            sum_str = 0
            count = 1
            for i in range(len(nums)):
                if sum_str + nums[i] <= _max:
                    sum_str += nums[i]
                else:
                    count += 1
                    sum_str = nums[i]
            # print(count)
            return count

        max_str = max(nums)
        sum_str = sum(nums)

        left = max_str
        right = sum_str

        while left < right:
            mid = left+ int((right-left)/2)
            if split(mid, nums) <= m:
                right = mid
            else:
                left = mid +1

        return left if left<= right else -1


sol = Solution()
print(sol.splitArray([7,2,5,10,8],2))