


def subset(nums):
    res = []
    def trackback(nums,i,track):

        res.append(track[:])
        # 这里要设置i的起始点，不然i每次递归进去之后都是从0开始，nums[0:]就是它本身
        for i in range(i,len(nums)):
            track.append(nums[i])
            trackback(nums,i+1,track)
            track.pop()
        # return res
    trackback(nums,0,[])
    return res




print(subset([1,2,3]))