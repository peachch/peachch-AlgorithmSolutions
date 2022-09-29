# def f(m, n):
#     if m == 0 or n == 1:
#         return 1
#     if m < n:
#         return f(m, m)
#
#     return f(m - n, n) + f(m, n - 1)
#
# print(f(7,3))
#
# _didct = {0:[1],1:[2]}
# _dict = sorted(_didct.keys())
# print(_dict)
# for k in _dict:
#     print(_didct[k])
# print(_dict)

_in = "12345"
# _in[0] = "2"
print(_in)
lo = 0
hi = len(_in)-1
_ii = ""
while lo < hi:

    lo+=1
    hi-=1
print(_ii)


print(int("0xAF",16))
print(bin(5))

a = [[1,2,3],[5,3,6],[7,4,2]]
print(map(max,a))