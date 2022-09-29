
def mainpathsum(grid):
    res = grid
    print(grid[0][0])
    #res[0][0] = grid[0][0]
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if i-1 >=0 and j-1 >=0:
                res[i][j] = min(grid[i-1][j] ,grid[i][j-1]) +grid[i][j]
            elif i-1 < 0 and j-1 >=0:
                res[i][j] = grid[i][j-1] + grid[i][j]
            elif j-1 <0 and i-1 >= 0:
                res[i][j] = grid[i-1][j] + grid[i][j]

    return res[int(len(grid))-1][int(len(grid[0])-1)]




grid = [[1,2,3],[4,5,6]]
print(mainpathsum(grid))