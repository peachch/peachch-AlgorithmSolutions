

nums = [1,2, 3]
print(id(nums))
a = nums[:]
b = nums[:]
a[0] = 30
b[0] = 40
print(id(a))
print(nums)