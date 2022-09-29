


def get_sum(target):
    res_list = []
    def dfs(target, path):
        if sum(path) == target and sorted(path) not in res_list:
            res_list.append(sorted(path[:]))
            return
        if sum(path) > target:
            return
        for num in range(1, target+1):
            path.append(num)
            dfs(target, path)
            path.pop()
        print(res_list)
        return len(res_list)
    return dfs(target, [])

print(get_sum(10))