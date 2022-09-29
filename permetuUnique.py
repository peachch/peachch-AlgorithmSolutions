def permetuUnique(nums):

    def backtrack(begin,path,track):
        if begin == len(nums) and track not in res:
            res.append(track[:])
            return res

        for i in range(len(nums)):
            if i in path:
                continue
            track.append(nums[i])
            path.append(i)
            backtrack(begin+1,path,track)
            track.pop()
            path.pop()

    res = []
    backtrack(0,[],[])
    return res

nums = [1,1,2]
print(permetuUnique(nums))