# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = deque([])
        stack.append(root)

        while stack:
            curr = stack.pop()

            if curr:
                temp = curr.left
                curr.left = curr.right
                curr.right = temp

                stack.append(curr.left)
                stack.append(curr.right)

        return root

    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node: Optional[TreeNode]) -> None:
            if not node:
                return None
            else:
                node.left, node.right = node.right, node.left
                invert(node.left)
                invert(node.right)
            return None

        invert(root)
        return root


"""
Test Case:
[3,2,1] -> [3,1,2]
root=[4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]


"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

"""
Approach:
Go through each node and swap order of left and right children
Visting each node is O(n), swapping is O(n) since each node is stored
"""