
import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        ascii_stack = [False for _ in range(256)]
        count = collections.Counter(s)
        print(count)
        for c in s:
            cc = ord(c)
            count[c] -= 1
            if ascii_stack[cc]: continue
            while stack and ord(stack[-1]) > cc and count[stack[-1]] >0:
                ascii_stack[ord(stack[-1])] = False
                stack.pop()

            ascii_stack[cc] = True
            stack.append(c)
        return "".join(c for c in stack)
        # print(ord(c for c in s))

sol = Solution()
print(sol.removeDuplicateLetters("bcabc"))