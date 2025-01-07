from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        stack = deque([root])
        height = {None: (0, 0)}
        # saving max height overall and the max height of the node
        # base case None, 0 height

        while stack:
            curr = stack[-1]  # last element check

            if curr.left and curr.left not in height:
                stack.append(curr.left)
            elif curr.right and curr.right not in height:
                stack.append(curr.right)
            else:
                curr = stack.pop()
                leftHeight, leftDiameter = height[curr.left]
                rightHeight, rightDiameter = height[curr.right]

                currHeight = max(leftHeight, rightHeight) + 1
                currDiameter = res = max(res, leftHeight + rightHeight)

                height[curr] = (currHeight, currDiameter)

        return res

    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return -1

            left = dfs(root.left) + 1
            right = dfs(root.right) + 1
            res = max(res, left + right)
            return max(left, right)

        dfs(root)
        return res

"""
Test Case:
root = [1,null,2,3,4,5] -> 3
root = [1,2,3] -> 2

"""

"""
Iterative
Time Complexity: O(n)
Space Complexity: O(n)


DFS
Time Complexity: O(n) 
Space Complexity: O(h) -> h is height of tree
"""

"""
Approach:
Visit each node and if the node is a leaf node, calculate it's height which is it's children plus 1

Visting each node takes O(n) and saving the height takes O(n)
"""