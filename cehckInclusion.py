import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = collections.Counter(s1)
        window = {}
        for c in need:window[c] = 0
        left = 0
        right = 0
        valid = 0
        lenth = len(s1)
        while right < len(s2):
            c = s2[right]
            right += 1
            if need[c]:
                window[c] += 1
                if window[c] == need[c]:
                    valid +=1
            # print(window)
            while valid == len(need):
                if right - left == lenth:
                    return True
                # lenth = right - left
                # print(lenth)
                # start = left
                s = s2[left]
                left += 1
                if need[s]:
                    if window[s] == need[s]:
                        valid -=1
                    window[s] -= 1
        return False


sol = Solution()
print(sol.checkInclusion(s1 = "ab" ,s2 = "eidbaooo"))