


def permute(nums):
    res = []
    def backtrack(nums,track):
        if len(track) == len(nums):
            res.append(track[:])
            return res
        for i in range(len(nums)):
            if nums[i] not in track:
                track.append(nums[i])
                backtrack(nums,track)
                track.pop()

    backtrack(nums,[])
    return res

print(permute([1,2,3]))
