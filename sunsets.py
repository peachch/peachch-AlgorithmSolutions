def subsuts(nums):

    def dfs(nums,track):
        res.append(track[:])
        for i in range(len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            dfs(nums[i:],track)
            track.pop()
        return res

    res = []
    dfs(nums,[])
    return res




print(subsuts([1,2,3]))

