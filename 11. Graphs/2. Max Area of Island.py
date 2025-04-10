class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):

            if min(i, j) < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            area = 1
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))

        return res

"""
Test Case:
Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

Output: 6
"""

"""
Time Complexity: O(m by n) -> n by m is board size
Space Complexity: O(m by n) -> board storage
"""

"""
Approach:
For every island, dfs and set all '1's to '0's and count the area of the island
"""