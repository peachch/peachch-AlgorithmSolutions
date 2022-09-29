class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        def isFinish(weights, days, n):
            i = 0
            day = 0
            # maxcap = n
            while day < days:
                maxcap = n
                # maxcap -= weights[i]
                while maxcap-weights[i] >= 0:
                    maxcap -= weights[i]
                    i += 1

                    if i == len(weights):return True
                day += 1

            return False

        sum_w = sum(weights)
        min_w = max(weights)
        left = min_w
        right = sum_w + 1
        while left < right:
            mid = left + int((right - left) / 2)
            if isFinish(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left

sol = Solution()
print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))

