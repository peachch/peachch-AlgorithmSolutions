def mainpathsum(grid):
    dp = [float('inf')] * (len(grid[0]) + 1)
    dp[1] = 0
    for row in grid:
        for idx, num in enumerate(row):
            dp[idx + 1] = min(dp[idx], dp[idx + 1]) + num
    return dp[-1]

grid = [[1,2,3],[4,5,6]]
print(mainpathsum(grid))