# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = {root: 1}
        stack = deque([root])

        while stack:
            curr = stack.pop()

            if curr.left:
                depth[curr.left] = depth[curr] + 1
                stack.append(curr.left)
            if curr.right:
                depth[curr.right] = depth[curr] + 1
                stack.append(curr.right)

        return max(depth.values())


"""
Test Case:
root = [1,2,3,null,null,4] -> 3
root = [] -> 0


"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

"""
Approach:
Go through each node and calculate it's depth
Visting each node is O(n), saving each depth is O(n)
"""