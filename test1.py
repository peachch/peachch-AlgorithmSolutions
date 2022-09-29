
import itertools



print("".join(["1","2","3"]))


listt = [1,2,3,3,4]
print(set(listt))

ids = [[1,2],[1,2]]
news_ids = set(ids)
news_ids = list(news_ids)
print(news_ids)
ids.sort()
print(ids)
it = itertools.groupby(ids)
for k, g in it:
    print(k)


print(2**2)