

def combine(n,k):
    res = []
    def backtrack(i,track):
        if len(track) == k:
            res.append(track[:])
            return res
        for i in range(i,n+1):
            track.append(i)
            backtrack(i+1,track)
            track.pop()

    backtrack(1,[])
    return res

print(combine(4,2))
