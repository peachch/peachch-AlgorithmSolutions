import collections
def checkInclusion(s1: str, s2: str) -> bool:
    need = collections.Counter(s1)
    window = collections.defaultdict(int)
    left = right = 0
    valid = 0
    start = 0
    lenth = len(s2)
    print(need)

    while right < len(s2):
        c = s2[right]
        right += 1
        if need[c]:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1
        # print(window)
        while right - left >= len(s1):
            # print(valid)
            if valid == len(need):
                print("here", window)
                return True
            d = s2[left]
            left += 1
            if need[d]:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
                print(window)

    return False


print(checkInclusion("ab","eiboaoo"))