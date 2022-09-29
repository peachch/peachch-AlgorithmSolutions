
def quanpailie(s):

    res = []
    def dfs(idx,path,id_path):
        res.append(path[:])
        if idx == len(s):
            return res

        for i in range(idx,len(s)):
            if i in id_path:continue
            id_path.append(i)
            path.append(s[i])
            dfs(idx+1,path,id_path)


        return res
    return dfs(0,[],[])

print(quanpailie("123"))
