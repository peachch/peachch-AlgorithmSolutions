def exist(board,word):
    # 这种方法会产生错误
    marked1 = [[False]*len(board[0])]*len(board)
    marked = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    print(marked)
    print(marked1)

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == word[0]:
                marked[row][col] = True
                print(marked[row][col])
                if judge(board,word[1:],row,col,marked):
                    return True
                else:
                    marked[row][col] = False
    return False

def judge(board,word,row,col,marked):
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    if len(word) == 0:
        return True

    for j in directions:
        cur_row = row + j[0]
        cur_col = col + j[1]
        if cur_row >= 0 and cur_col >= 0 and cur_col < len(board[0])\
            and cur_row < len(board) and board[cur_row][cur_col] == word[0]:
            if marked[cur_row][cur_col] == True:
                continue
            marked[cur_row][cur_col] = True
            if judge(board,word[1:],cur_row,cur_col,marked) == True:
                return True
            else:
                marked[cur_row][cur_col] = False

    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(exist(board,word))