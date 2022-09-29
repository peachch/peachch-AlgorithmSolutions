
def threeSum(nums):
    def twoSum(nums,start,target):
        res = []
        low = start
        high = len(nums)-1

        while low < high:
            left = nums[low]
            right = nums[high]
            sum = nums[low] + nums[high]
            if sum < target:
                while low < high and nums[low] == left:
                    low += 1
            elif sum > target:
                while low < high and nums[high] == right:
                    high -= 1
            elif sum == target:
                res.append([left,right])
                while low < high and nums[low] == left:
                    low += 1
                while low < high and nums[high] == right:
                    high -= 1
        return res

    nums = sorted(nums)
    lenth = len(nums)
    res = []
    i = 0
    while i < lenth-1:
        target= 0 - nums[i]
        tuples = twoSum(nums,i+1,target)
        for tu in tuples:
            tu.append(nums[i])
            res.append(tu)
        # 这里在选择完之后再进行相同移位，不然会将可以作为元素的相同数漏掉，导致结果错误。
        while i < lenth - 1 and nums[i] == nums[i + 1]: i += 1
        i += 1

    return res
print(threeSum([-1,0,1,2,-1,-4]))