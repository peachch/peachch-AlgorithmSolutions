import heapq
class Solution:
    #
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        print(q)
        ans = [-q[0][0]]
        print(ans)
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans

class MontonicQueue():
    queue = []
    def __init__(self):
        self.queue = MontonicQueue.queue
    def push(self,n):
        while self.queue and self.queue[-1] < n:
            self.queue.pop()
        # print(self.queue)
        self.queue.append(n)
        # print(self.queue)
    def max(self):
        return self.queue[0]
    def pop(self,n):
        if n == self.queue[0]:
            self.queue.pop(0)

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],2))