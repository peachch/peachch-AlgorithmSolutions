import collections
def lengthOfLongestSubstring(s: str) -> int:
    left = right = 0
    window = collections.defaultdict(int)
    maxsub = 0
    while right < len(s):

        c = s[right]
        right+= 1

        window[c] += 1
        # 当出现大于1时，就开始收缩窗口
        while window[c] > 1:
            cc = s[left]
            left += 1
            # 这里的cc就是刚才的c，所以这里对cc进行减操作，就是对刚才的c进行操作，所以while不会一直保持为1
            window[cc] -= 1
        maxsub = max(maxsub, right - left)
    return maxsub

print(lengthOfLongestSubstring("abcabcbb"))