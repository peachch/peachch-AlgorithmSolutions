class Solution:
    def sortArray(self, nums):
        def partition(nums, lo, hi):
            if lo == hi: return lo
            # 指针
            p = nums[lo]
            i = lo+1
            j = hi
            while True:
                while nums[i] < p:
                    i += 1
                    if i >= hi: break

                while nums[j] > p:
                    j -= 1
                    if j == lo: break
                if i >= j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            nums[lo], nums[j] = nums[j], nums[lo]
            print(nums)
            return j

        def sort(nums, lo, hi):
            if lo >= hi: return
            p = partition(nums, lo, hi)
            sort(nums, lo, p - 1)
            sort(nums, p + 1, hi)

        sort(nums, 0, len(nums) - 1)
        return nums

sol=Solution()
sol.sortArray([3,-1])