def permute(nums):

    def dfs(nums,track):
        if len(track) == len(nums):
            res.append(track[:])

        for i in nums:
            if i in track:
                continue

            track.append(i)
            dfs(nums,track)
            # 在这里回退
            track.pop()
        return res

    track = []
    res = []
    dfs(nums,track)
    return res




print(permute(nums=[1,2,3]))
