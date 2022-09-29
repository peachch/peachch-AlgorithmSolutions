def knapsack(W, N, wt, val):
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for n in range(1,N+1):
        for w in range(1,W+1):
            if w - wt[n-1] <0:
                dp[n][w] = dp[n-1][w]
            else:
                dp[n][w] = max(dp[n-1][w-wt[n-1]] + val[n-1],dp[n-1][w])
    return dp[N][W]

print(knapsack(4,3,[2,1,3],[4,2,3]))
