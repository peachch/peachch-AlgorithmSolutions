



def canJump(nums):
    k =0
    for i in range(len(nums)):

        if i>k :
            return False
        k = max(k,i + nums[i])
    return True



print(canJump([3,2,1,0,4]))