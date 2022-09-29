class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        right = 0
        res = 0
        for c in s:
            if c == "(":
                right += 2
                if right %2 ==1:
                    res += 1
                    right -= 1

            else:
                right -= 1
                if right == -1:
                    res += 1
                    right =1
        return res + right

sol = Solution()
print(sol.minInsertions("(()))(()))()())))"))