def exsist(board,word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == list(word)[0]:
                for z in range(1,len(list(word))):
                    def dfs(word):
                        if word[z] == board[i][j+1]:
                            
    return ""

board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
word = "ABCCED"

exsist(board,word)