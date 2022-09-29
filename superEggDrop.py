class Solution:
    def superEggDrop(self,K, N) -> int:

        memo = dict()
        def dp(K,N) -> int:
            if K == 1: return N
            if N == 0: return 0

            # res = float('INF')
            if (K,N) in memo:
                return memo[(K,N)]

            res = float('INF')

            for i in range(1, N+1):
                res = min(res,
                          max(
                              dp(K, N - i),
                              dp(K-1, i-1)
                ) +1
                          )

            memo[(K,N)] = res
            print(memo)
            return res

        return dp(K,N)


sol=Solution()
print(sol.superEggDrop(2,74))

