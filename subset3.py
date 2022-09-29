def subsets(nums):

    def backtrack(begin,track):

        if track not in res:
            res.append(track)
        # if depth == len(nums):
        for i in range(begin,len(nums)):
            backtrack(i+1,track + [nums[i]])


    res =[[]]
    backtrack(0,[])
    return res

nums = [4,4,4,1,4]
print(subsets(sorted(nums)))