# 这个题用不到剪枝，因为从边界出发的话，只要有，就一定是要被设置成O。用不到剪枝 所以严格意义上来说，是深度优先遍历的做法，并不是回溯
# 因为这个题是要原地修改，所以需要将要改变的位置，修改为B，之后再把B修改为O。

def solve(board):
    def trackback(row, col, board):

        directions = ([0, 1], [0, -1], [1, 0], [-1, 0])
        board[row][col] = "B"
        for i in directions:
            cur_row = i[0] + row
            cur_col = i[1] + col

            if 0 <= cur_row < len(board) and 0 <= cur_col < len(board[0]) and board[cur_row][cur_col] == "O":
                trackback(cur_row,cur_col,board)
                    #track.append([cur_row, cur_col])

        return board
    track =[]
    marked = [[False for _ in range(len(board))] for _ in range(len(board[0]))]
    for row in range(len(board)):
        for col in range(len(board[0])):
            if row == 0 or row ==len(board)-1 or \
                col == 0 or col == len(board[0])-1:
                if board[row][col] == "O":

                    trackback(row,col,board)
                    # res = [["X" for _ in range(len(board))] for _ in range(len(board[0]))]
                    # board = [["X" for _ in range(len(board))] for _ in range(len(board[0]))]

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "B":
                board[row][col] = "O"
            elif board[row][col] == "O":
                board[row][col] = "X"

    return board

board =[["X","X","X","X"],["X","O","X","X"],["X","X","X","X"],["X","O","X","X"]]
print(solve(board))