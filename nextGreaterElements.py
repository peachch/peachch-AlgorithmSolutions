class Solution:
    def nextGreaterElements(self, nums ):
        new_nums = nums[:]
        new_nums.extend(nums)
        print(new_nums)
        stack = []
        res = [0 for i in range(len(new_nums))]
        for i in range(len(new_nums)):
            while stack and stack[-1] <= new_nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            else:
                res[i] = -1
            stack.append(new_nums[i])
            print(stack)
        return res[:len(nums)]

sol = Solution()
print(sol.nextGreaterElements([1,2,1]))