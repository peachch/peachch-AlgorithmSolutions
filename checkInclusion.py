import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = collections.Counter(s1)
        valid = 0
        window = {}
        for c in s1:window[c] = 0
        left = right =0
        while right < len(s2):
            c = s2[right]
            right+=1
            if need[c]:
                window[c] +=1
                if window[c] == need[c]:
                    valid+=1
            # 不同的题目要求这里不一样，也就是需要定义何时开始收缩
            while right-left >= len(s1):
                # 这里是输出结果的地方，这里的条件对结果进行约束
                if len(window) == valid:
                    return True
                d = s2[left]
                left += 1
                if need[d]:
                    if window[d] == need[d]:
                        valid-=1
                    window[d] -= 1
        return False

sol=Solution()
print(sol.checkInclusion("abcdxabcde","abcdeabcdx"))