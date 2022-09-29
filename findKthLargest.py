class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        def partition(nums, lo, hi):
            if lo == hi: return lo
            def swap(nums,i,j):
                nums[i],nums[j] = nums[j],nums[i]

            pro = nums[lo]
            i = lo
            j = hi+1
            while True:
                i += 1
                while nums[i] < pro:
                    if i == hi: break
                    i += 1
                j-= 1
                while nums[j] > pro:
                    if j == lo: break
                    j -= 1
                if i >= j: break
                swap(nums,i,j)
            swap(nums,j,lo)
            return j

        lo = 0
        hi = len(nums) - 1
        kk = len(nums) - k

        while lo <= hi:
            p = partition(nums, lo, hi)
            if p > kk:
                hi = p - 1
            elif p < kk:
                lo = p + 1
            else:
                return nums[p]
        return -1

sol = Solution()

print(sol.findKthLargest([3,3,3,3,3,3,3,3,3],1))