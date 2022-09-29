class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        import collections
        stack = []
        res = []
        mappins = collections.Counter(s)
        for c in s:
            if c in stack: continue
            while stack and ord(c) < ord(stack[-1]) and mappins[stack[-1]] >= 1:
                stack.pop()

            stack.append(c)
            mappins[c] -= 1

        return "".join(stack)


sol = Solution()
print(sol.removeDuplicateLetters("bbcaac"))