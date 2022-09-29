def getPermutation(n,k):

    def trackback(depth,track):

        if len(track) == n:
            res_list.append(track[:])
            return res_list
        if len(res_list) == k:
            return
        if len(res_list) < k :
            for i in range(1,n+1):
                if i in track:
                    continue
                track.append(i)

                trackback(depth+1,track)
                track.pop()
            return
        return

    res_list = []
    trackback(1,[])
    return "".join(str(i) for i in res_list[k-1])

n=3
k=2
print(getPermutation(n,k))