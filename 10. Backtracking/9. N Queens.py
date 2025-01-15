class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(currRow, currCol, sol, diag1, diag2, row, col):

            # print(currRow, row, currCol, col)
            if len(row) == n:
                res.append(sol)
                return

            for i in range(n):
                for j in range(n):
                    if i not in row and j not in col and i + j not in diag1 and i - j not in diag2:
                        dfs(i, j, sol + [(i, j)], diag1 + [i + j], diag2 + [i - j], row + [i], col + [j])

        dfs(0, 0, [], [], [], [], [])

        unique = []
        for i in res:
            i.sort()
            unique.append(tuple(i))
        unique = list(set(unique))

        res = []
        for i in unique:
            print(i)
            board = [["."] * n for i in range(n)]

            for q in i:
                board[q[0]][q[1]] = "Q"

            sol = ["".join(j) for j in board]
            res.append(sol)

        print(res)

        return res