class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(char, row, col):
            for i in range(9):
                if board[i][col] == f"{char}":
                    return False
                if board[row][i] == f"{char}":
                    return False
                # 这里可以思考为，当i=1时，应该遍历[0][0] [0][1] [0][2],所以column部分应该用余数来做，row不变，所以可以用除数来做。
                if board[int(row / 3) * 3 + int(i / 3)][int(col / 3) * 3 + (i % 3)] == f"{char}":
                    return False
            return True

        def trackback(board, row, col):
            if col == 9:
                return trackback(board, row + 1, 0)
            if row == 9:
                return board
            i = row
            j = col
            while i < 9:
                while j <9:
                    if board[i][j] != ".":
                        return trackback(board,i,j+1)
                    for char in range(1, 10):
                        if not isValid(char, i, j):
                            continue
                        board[i][j] = f"{char}"
                        # 只有当row==9时，这里才有值，只要找到符合的，则直接返回，跳出所有循环。
                        # 如果这里没值，就会重置为"."，回溯
                        if trackback(board, i, j + 1):
                            return board
                            # return True
                        board[i][j] = "."
                    j+=1
                    # 当列没有合适的时候，跳出，保证每个值都被处理到，如果这里没有，则
                    return
                i+=1
            # 当前没有合适的值，跳出，回到if trackback()的判断
            return

        # row = len(List[0])
        # col = len(List)
        trackback(board, 0, 0)
        return board

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
print(sol.solveSudoku(board))





