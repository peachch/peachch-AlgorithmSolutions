def uniquePaths(m, n):
    dparray = [[1]*n]*m
    print(dparray)
    for i in range(m):
        for j in range(n):
            if i-1 >=0 and j-1 < 0 :
                dparray[i][j] = dparray[i-1][j]
            elif j-1 >=0 and i-1 < 0 :
                dparray[i][j] = dparray[i][j-1]
            elif i-1 >=0 and j-1 >= 0:
                dparray[i][j] = dparray[i][j-1] + dparray[i-1][j]

    return dparray[m-1][n-1]

m = 3
n = 7
print(uniquePaths(m,n))