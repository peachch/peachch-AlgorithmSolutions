def permetuUnique(nums):

    def backtrack(begin,path,track,size):
        if begin == size:
            res.append(track[:])
            return res

        for i in range(size):
            if not path[i]:
                if i>0 and path[i-1] == False and nums[i]==nums[i-1]:
                    continue
                track.append(nums[i])
                path[i] = True
                backtrack(begin+1,path,track,size)
                path[i] = False
                track.pop()


    res = []
    size = len(nums)
    path = [False]*size
    print(path)
    backtrack(0,path,[],size)
    return res

nums = [3,3,0,3]
print(permetuUnique(sorted(nums)))