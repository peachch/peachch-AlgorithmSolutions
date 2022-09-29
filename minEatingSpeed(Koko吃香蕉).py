class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        def canFinish(piles,n,h):
            time_item = 0
            for item in piles:
                time_item += int((item/n)) + (1 if item%n>0 else 0)
            if time_item <= h:
                return True
            return False
        maxnum = max(piles)
        print(maxnum)
        left = 1
        right = maxnum + 1
        while left < right:
            mid = left + int((right-left)/2)
            if canFinish(piles,mid,h):
                right = mid
            else:
                left = mid + 1
        return left


sol = Solution()
print(sol.minEatingSpeed([3,6,7,11],8))