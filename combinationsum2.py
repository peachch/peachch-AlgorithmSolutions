def combinationsum2(nums,target):
    def backtrack(begin,track,residue):
        print(nums)
        if residue == 0:
            res.append(track[:])
            return res
        # range表示计数从begin这个值开始 而不是begin之后 到size前一位截止，这里清晰一下
        for i in range(begin,len(nums)):
            if nums[i] > residue:
                # 看一下break和return的区别
                break
            if i > begin and nums[i] == nums[i-1]:
                # continue只跳过当前，break从当前位置直接跳出，这里脑子清晰一点
                continue
            track.append(nums[i])
            backtrack(i+1,track,residue-nums[i])
            track.pop()
    res = []
    backtrack(0,[],target)
    return res


nums = [10,1,2,7,6,1,5]
nums_ = sorted(nums)
print(nums_)
print(combinationsum2(nums_,8))