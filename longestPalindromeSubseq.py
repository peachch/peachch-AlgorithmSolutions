class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        j = 0
        i = len(s)-1
        dp = [[0 for _ in range(i+1)] for _ in range(i+1)]
        for z in range(i+1):
            dp[z][z] = 1

        while i  >= 0:
            j = i+1
            while j < len(s):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
                j += 1
            i -= 1

        return dp[0][len(s)-1]


sol = Solution()
print(sol.longestPalindromeSubseq("bbbab"))