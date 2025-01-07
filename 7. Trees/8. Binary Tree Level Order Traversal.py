# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        queue = deque([root])
        '''
        Basically we want to do bfs and each level put the result in a new sublist
        '''

        res = []
        depth = {root: 0}
        level = 0
        if not root:
            return res

        while queue:
            curr = queue.popleft()

            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
                depth[curr.left] = depth[curr] + 1
                depth[curr.right] = depth[curr] + 1

                level = depth[curr]
                if len(res) - 1 < level:
                    currList = [curr.val]
                    res.append(currList)
                else:
                    currList = res[level]
                    currList.append(curr.val)

        return res


"""
Test Case:
root = [1,2,3,4,5,6,7] -> [[1],[2,3],[4,5,6,7]]
root = [1] -> [[1]]
root = [] -> []


"""

"""
Iterative
Time Complexity: O(n)
Space Complexity: O(n)


DFS
Time Complexity: O(n) 
Space Complexity: O(n)
"""

"""
Approach:
BFS visit each node and keep track of the given depth of the node, the node is inserted into res[depth] at it's depth
Can be done with dfs, just keep track of the depth of each node
"""