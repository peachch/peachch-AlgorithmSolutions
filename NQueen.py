import copy


class Solution:
    def solveNQueens(self, n: int) :
        def isValid(board, row, col):
            for i in range(n):
                if board[i][col] == "Q":
                    return False
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            ii = row - 1
            jj = col -1
            while ii >= 0 and jj >= 0:
                if board[ii][jj] == "Q":
                    return False
                ii -= 1
                jj -= 1
            return True

        def backtrack(board, row):
            if row == n:
                string_board = copy.deepcopy(board)
                for i in range(n):
                    print(string_board[i])
                    string_board[i] = "".join(string_board[i])
                print("sss",string_board)
                res.append(string_board)
                print("ssss",id(i for i in res))
                return res
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                board[row][col] = "Q"
                backtrack(board, row + 1)
                board[row][col] = "."
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        backtrack(board, 0)
        return res

sol = Solution()
print(sol.solveNQueens(4))