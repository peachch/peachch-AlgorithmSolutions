class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        right = sum(weights)
        left = max(weights)

        def can_load(weights, canload):
            day = 0
            i = 0
            while i < len(weights):
                sum_load = 0
                while i < len(weights) and sum_load + weights[i] <= canload:
                    sum_load = sum_load + weights[i]
                    i += 1
                    continue
                day += 1
            return day

        while left <= right:
            mid = left + int((right - left) / 2)
            this_day= can_load(weights, mid)
            if this_day > days:
                left = mid + 1
            elif this_day < days:
                right = mid - 1
            elif this_day == days:
                right = mid - 1
        return left


sol = Solution()
print(sol.shipWithinDays([1,2,3,1,1], 4))