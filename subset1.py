def subsets(nums):

    res = [[]]

    for i in nums:
        res = res + [[i]+ j for j in res]
    return res


nums = [1,2,3]
print(subsets(nums))