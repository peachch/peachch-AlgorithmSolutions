class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        diff = [0 for _ in range(1001)]
        nums = [0 for _ in range(1001)]
        for trip in trips:
            num = trip[0]
            start = trip[1]
            end = trip[2] - 1
            diff[start] += num
            if end < 1000:
                diff[end+1] -= num
        nums[0] = diff[0]
        print(diff)
        for i in range(1,1001):
            nums[i] = nums[i-1] + diff[i]
            if nums[i] > capacity:
                return False
        return True

sol= Solution()
print(sol.carPooling([[9,0,1],[3,3,7]],4))