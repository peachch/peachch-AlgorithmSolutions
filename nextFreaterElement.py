class Solution:
    def nextGreaterElement(self, nums1, nums2):
        i = len(nums2)-1
        mapping = {}
        for j in nums2: mapping[j] = -1
        stack = []
        while i >= 0:
            if stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                mapping[nums2[i]] = stack.pop()
            stack.append(nums2[i])
            i -= 1
        res =[]
        for i in nums1:
            res.append(mapping[i])
        return res

sol = Solution()
print(sol.nextGreaterElement([2,4],[1,2,3,4]))