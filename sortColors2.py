def sortColors(nums):
    p1=len(nums)-1
    p0=0
    i = 0
    while i <= p1:
        if nums[i] == 0:
            nums[i], nums[p0] = nums[p0],nums[i]
            p0 += 1
            i+=1
        elif nums[i] == 2:
            nums[i], nums[p1] = nums[p1],nums[i]
            p1 -= 1
        else:
            i+=1
    return nums

nums1 = [2,0,2,1,1,0]

print(sortColors(nums1))