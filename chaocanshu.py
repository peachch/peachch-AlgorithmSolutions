
import numpy as np
def dp(str):
    lenth = len(str)
    visited = [False for _ in range(lenth)]
    dp_table = [[0 for _ in range(lenth)] for _ in range(lenth)]
    j = 0
    while j < lenth:
        i = 0
        while i < j:
            if not visited[j]:
                if str[i] == str[j]:
                    if not visited[i]:
                        visited[j] = True
                        visited[i] = True
                        dp_table[i][j] = max(dp_table[i][j], dp_table[i - 1][j - 1] + 1)
            i+=1
        visited[i] = False
        visited[j] = False
        j+=1
    print(dp_table)


str = "aaaab"
dp(str)


