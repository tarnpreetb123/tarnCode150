class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        def dfs(row, sol, diag1, diag2):

            if row == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return

            for col in range(n):
                if col not in sol and row + col not in diag1 and row - col not in diag2:
                    board[row][col] = 'Q'
                    dfs(row + 1, sol + [col], diag1 + [row + col], diag2 + [row - col])
                    board[row][col] = '.'

        dfs(0, [], [], [])

        return res

"""
Test Case:
Input: n = 4

Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

Input: n = 1

Output: [["Q"]]

"""

"""
Time Complexity: O(n!) -> given n rows, we are trying column options which leads to n! choices to make
Space Complexity: O(n^2) ->  n by n board size, sol, diag1, diag2 are n but the board is n by n
"""

"""
Approach:
For every digit, go through all letters and dfs down the graph, if the graph ends then the base case takes over the the sol is added to results

"""