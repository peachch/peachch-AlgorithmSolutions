def sortColors(nums) -> None:
    p1=0
    p0=0
    for i in range(len(nums)):
        if nums[i] == 1:
            nums[i] , nums[p1] =nums[p1],nums[i]
            p1 += 1
        if nums[i] == 0:
            nums[i], nums[p0] = nums[p0],nums[i]
            if p0 < p1:
                nums[i],nums[p1] = nums[p1],nums[i]
            p0 += 1
            p1 += 1
    return nums

nums1 = [2,1]

print(sortColors(nums1))

