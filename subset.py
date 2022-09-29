def subsets(nums):
    res = []
    n = len(nums)

    def helper(i, tmp):
        res.append(tmp)
        print(res)
        for j in range(i, n):
            helper(j + 1, tmp + [nums[j]])

    helper(0, [])
    return res



nums = [1,2,3]
print(subsets(nums))