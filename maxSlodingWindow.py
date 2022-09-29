import collections
class Solution:

    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        q = collections.deque()
        ans = []
        # 先放入前k个元素中最大的
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        # 存入结果
        ans.append(nums[q[0]])
        for i in range(k,n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            # 从左边pop掉不属于window的元素
            while q[0] <= i -k:
                q.popleft()
                # print(q)
            ans.append(nums[q[0]])
        # print(q)
        return ans


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],2))