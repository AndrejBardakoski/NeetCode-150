from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            d = {}
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in d:
                        return False
                    d[board[i][j]] = True

        for i in range(9):
            d = {}
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in d:
                        return False
                    d[board[j][i]] = True

        for i in range(9):
            d = {}
            for j in range(9):
                a = (i // 3) * 3 + j // 3
                b = (i % 3) * 3 + j % 3
                if board[a][b] != '.':
                    if board[a][b] in d:
                        return False
                    d[board[a][b]] = True
        return True
