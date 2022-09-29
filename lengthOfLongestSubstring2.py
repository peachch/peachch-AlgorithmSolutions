class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window = {}
        res = 0
        for i in s: window[i] = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            # res+=1
            while window[c] > 1:
                d = s[left]
                left += 1
                if window[d]:
                    window[d] -= 1
        # 更新res的位置是更新完left之后，因为while的条件是存在重复元素，更新完之后才可以保证不存在重复元素，所以在这里更新
        res = max(res, right - left)
        return res

sol = Solution()
print(sol.lengthOfLongestSubstring("aab"))