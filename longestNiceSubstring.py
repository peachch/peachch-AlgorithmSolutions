class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        window = []
        lenth = len(s)
        lo = 0
        hi = 0
        # window.append(s[0])
        re = {}
        res = 0
        valid = []
        while hi < lenth-1:
            c = s[hi]
            hi += 1
            while lo < hi - 1 and ord(s[hi]) != ord(s[lo]) or ord(s[hi]) != ord(s[lo]) + 32 or ord(
                    s[hi]) != ord(s[lo]) - 32:
                # valid.append(s[hi])
                window.append(c)
                print("window", lo, hi)
                lo += 1
            if window:
                res = max(res, len(window))
                if not re.get(res):
                    re[res] = window

        return re[res]

sol=Solution()
print(sol.longestNiceSubstring("YazaAay"))