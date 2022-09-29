
def restorAddress(s):
    def trackback(track):
        temp = track.split(".")
        if len(temp) == 4:
            res.append(track)
            return res
        for i in range(0,3):
            if s[i]>= 0 and s[i] <= 255:
                track.join(s[i]+".")

            trackback(i+1,track)

    res =[]
    trackback("")
    return res

s = "010010"
print(int(s[1]+s[2]))
#["0.10.0.10","0.100.1.0"]
# print(restorAddress(s))