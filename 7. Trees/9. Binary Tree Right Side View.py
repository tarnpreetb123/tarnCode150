from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:

        if not root:
            return []
        # BFS and only include the last element per level
        res = []
        queue = deque([root])

        while queue:
            levelQ = len(queue)

            for i in range(levelQ):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                if i == levelQ - 1:
                    res.append(curr.val)

        return res


"""
Test Case:
root = [1,2,3] -> [1,3]
root = [1,2,3,4,5,6,7] -> [1,3,7]

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
BFS visit each node and the last node of that level is the one viewed from the right side, so add it to result
"""