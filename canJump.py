



def canJump(nums):
    n = len(nums)
    def res(index):
        if index == n - 1:
            return True
        for j in range(1,nums[index]+1):
            if res(j+index):
                return True
        return False
    return res(0)

print(canJump([2,3,1,1,4]))