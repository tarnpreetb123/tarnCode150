class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):

            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == '0':
                return

            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)

        return res

"""
Test Case:
Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4

"""

"""
Time Complexity: O(m by n) -> n by m is board size
Space Complexity: O(m by n) -> board storage
"""

"""
Approach:
For every island, dfs and set all '1's to '0's 
"""