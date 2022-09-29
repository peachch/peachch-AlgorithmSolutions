
def minEatingSpeed(piles, h: int) -> int:
    def check(base):
        H = 0
        for j in piles:
            if j % base > 0:
                H += int(j / base) + 1
            else:
                H += j / base
        return H <= h

    lf = 1
    rt = max(piles) + 1
    print(rt)
    while lf < rt:
        mid = lf + int((rt - lf) / 2)
        print(mid)
        if check(mid):
            rt = mid
            print("rt", rt)
        else:
            print(mid)
            lt = mid + 1
            print("lt", lt)
    return lf





