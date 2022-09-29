class Solution:
    def searchRange(self, nums, target: int):
        res =[]
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left+int((right-left)/2)
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid -1
            elif nums[mid] == target:
                right = mid -1
        if left >=len(nums) or nums[left]!= target:res.append(-1)
        else:
            res.append(left)
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left+int((right-left)/2)
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid -1
            elif nums[mid] == target:
                left = mid+1
        if right < 0 or nums[right]!=target:res.append(-1)
        else:
            res.append(left-1)
        return res

sol= Solution()
print(sol.searchRange(
[5,7,7,8,8,10],6
))