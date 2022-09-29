



def target(nums,target):
    res = []
    def dfs(nums, target, path):
        if sum(path) == target and path not in res:
            res.append(path[:])
            return res
        if sum(path) > target:
            return

        for num in nums:
            path.append(num)
            dfs(nums, target, path)
            path.pop()

        return res

    return dfs(nums,target,[])

print(target([1,2,3], 4))