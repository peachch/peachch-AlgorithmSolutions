class Solution:
    def longestPalindrome(self, s: str) -> str:
        def dp(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return "".join(s[i + 1:j])

        res = ""
        for i in range(len(s)):
            s1 = dp(i, i)
            s2 = dp(i, i + 1)
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res

sol =Solution()
print(sol.longestPalindrome("babad"))

s = [1,2,3,4,5]
print(s[2:4])