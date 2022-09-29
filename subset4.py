def subsets(nums):

    def backtrack(begin,track,path):

        res.append(track)
        for i in range(begin, len(nums)):
            if not path[i]:
                if i>0 and nums[i]==nums[i-1] and not path[i-1]:
                    continue

                path[i] =True
                backtrack(i+1,track+[nums[i]],path)
                path[i] = False


    res =[]
    path = [False]*len(nums)
    backtrack(0,[],path)
    return res

nums = [1,1,2,2]
print(subsets(sorted(nums)))