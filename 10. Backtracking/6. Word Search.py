class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        rows = len(board)
        cols = len(board[0])

        def search(board):
            for i in range(rows):
                for j in range(cols):
                    dfs(board, set(), i, j, 0)

        def dfs(board, visited, i, j, index):
            nonlocal res

            if index == len(word):
                res = True
                return True

            if index >= len(word) or i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in visited or board[i][j] != word[index]:
                return False

            print(visited, i, j, index, board[i][j])

            visited.add((i, j))
            local_res = (
                dfs(board, visited, i + 1, j, index+1) or
                dfs(board, visited, i - 1, j, index+1) or
                dfs(board, visited, i, j + 1, index+1) or
                dfs(board, visited, i, j -1, index+1)
            )
            visited.remove((i,j))
            return local_res
        search(board)
        return res

"""
Test Case:
Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true

"""

"""
Time Complexity: O(n*m*4^k) -> n by m is board size but for each square, searching 4 directions upwards of length of word
Space Complexity: O(n)
"""

"""
Approach:
For every single cell in the board, dfs recursively for the word. If the letter matches, search the neighbouring cells
while making sure not to use duplicate, if the letter doesn't match backtrack.
"""