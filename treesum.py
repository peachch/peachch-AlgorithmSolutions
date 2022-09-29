class Solution:
    def threeSum(self, nums):
        def twoSum(new_nums,start,target):
            low = start
            hight = len(new_nums)-1
            res = []
            while low < hight:
                _sum = new_nums[low] + new_nums[hight]
                left = new_nums[low]
                right = new_nums[hight]
                if _sum == target:
                    res.append([new_nums[low],new_nums[hight]])
                    while low< hight and new_nums[low] == left:low+=1
                    while low < hight and new_nums[hight] == right: hight -= 1
                elif _sum < target:
                    while low< hight and new_nums[low] == left:low += 1

                elif _sum > target:
                    while low< hight and new_nums[hight] == right:hight -=1
            print(res)
            return res
        res = []
        new_nums = sorted(nums)
        i = 0
        while i < len(new_nums):
            other = 0 - new_nums[i]
            result = twoSum(new_nums,i+1,other)
            if result:
                for ii in result:
                    ii.append(new_nums[i])
                    res.append(ii)
            while i < len(new_nums)-1 and new_nums[i] == new_nums[i+1]:
                i+=1
            i+=1
        return res

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))