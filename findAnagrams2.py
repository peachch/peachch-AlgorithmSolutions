import collections
class Solution:
    def findAnagrams(self, s: str, p: str):
        need = collections.Counter(p)
        window = {}
        for c in need:window[c] = 0
        left = 0
        right = 0
        valid = 0
        res = []
        lenth = len(p)
        while right < len(s):
            c = s[right]
            right+=1
            if need[c]:
                window[c] +=1
                if window[c] == need[c]:
                    valid+=1
            while valid == len(need):
                if len(p) == right-left:
                    # 这个在这里更新，是因为符合valid的条件和也就是题目要求的条件。
                    res.append(left)
                d = s[left]
                left += 1
                if need[d]:
                    if need[d] == window[d]:
                        valid-=1
                    window[d] -=1


        return res

sol = Solution()
print(sol.findAnagrams(
"cbaebabacd","abc"))