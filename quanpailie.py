def quanpailie(nums):
    res = []
    def backtrack(nums,track):
        if len(nums) == len(track):
            # 记得这里要用track[:],因为python中只是把track所指的对象，赋到res上，所以随着track的改变，res也会
            # 改变，所以用[:]表示将track通过切片得到的新对象append到res上。
            res.append(track[:])
            return
        for i in nums :
            if i in track:
                continue
            track.append(i)
            backtrack(nums,track)
            del(track[-1])

    backtrack(nums, [])
    return res

track = []
nums = [1,3,2]
print(quanpailie(nums))