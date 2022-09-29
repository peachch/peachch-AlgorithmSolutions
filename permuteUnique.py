class Solution:
    def permuteUnique(self, nums):
        def backtrack(begin,nums,track,path):
            if begin == len(nums):
                res.append(track[:])
                # print(res)
                return res
            for i in range(len(nums)):
                if  not path[i]:
                    # 这里避免重复的起始值
                    if i>0 and path[i-1] == False and nums[i] == nums[i-1]:
                        continue
                    track.append(nums[i])
                    path[i] = True
                    backtrack(begin+1,nums,track,path)
                    track.pop()
                    path[i] = False

        path = [False for _ in range(len(nums))]
        res = []
        backtrack(0,nums,[],path)
        return res


sol = Solution()
print(sol.permuteUnique([1,1,2]))