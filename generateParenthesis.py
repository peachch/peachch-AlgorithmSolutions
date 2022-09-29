def gen(n):
    def trackback(left,right,track,res):

        if left==0 and right==0:
            res.append(track)
            return res
        if left > right:
            return
        if left > 0:
            trackback(left-1,right,track+"(",res)

        if right >0 :
            trackback(left,right-1,track+")",res)

    res =[]
    trackback(n,n,"",res)
    return res


print(gen(2))