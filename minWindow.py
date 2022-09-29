import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        lenth = float("inf")
        start = 0
        valid = 0
        window = {}
        for c in t:window[c] = 0
        left = right = 0
        while right < len(s):
            word = s[right]
            right+=1
            if need[word]:
                window[word]+=1
                if window[word] == need[word]:
                    valid+=1
            print(window)
            while len(need) == valid:
                while left < right:
                    if lenth > right-left:
                        start = left
                        lenth = right-left
                    word_l = s[left]
                    left+=1
                    if need[word_l]:
                        if need[word_l] == window[word_l]:
                            valid-=1
                        window[word_l]-=1
        return "" if lenth == float("inf") else s[start:start+lenth]

sol=Solution()
print(sol.minWindow("ADOBECODEBANC","ABC"))