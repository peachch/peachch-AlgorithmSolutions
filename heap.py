









import heapq
def knn(k,P,m):
    def distance(m, p):
        return 1

    position = {}
    heap = []
    for p in P:
        distance = distance(m,p)
        heapq.heappush(heap, -distance)
        if len(heap) <= k:
            position.setdefault(distance,[]).append(p) #记录坐标

        if len(heap) > k:
            cur_dis = heapq.heappop(heap)
            if -distance < cur_dis:
                heapq.heappush(heap, -distance)
            else:
                heapq.heappush(heap, cur_dis)

    res = []
    for distance in heap:
        res.append(position[distance])
        if len(res) >= k:
            return res[:k+1]



