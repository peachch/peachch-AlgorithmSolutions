
import collections

def findAnagrams(s: str, p: str) :
    left = right = 0
    need = collections.Counter(p)
    window = collections.defaultdict(int)
    valid = 0
    res = []
    while right < len(s):
        c = s[right]
        right += 1
        if need[c]:
            window[c] += 1
            if need[c] == window[c]:
                valid += 1

        while right - left >= len(p):
            # 这里是用need的长度，因为上面valid已经判断了个数，所以这里只要保证有，则就示为正确了
            if valid == len(need):
                res.append(left)
            cc = s[left]
            left += 1
            if need[cc]:
                if need[cc] == window[cc]:
                    valid -= 1
                window[cc] -= 1
    return res

print(findAnagrams("ababv","aba"))



