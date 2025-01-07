# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = True

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) > 1:
                res = False

            return max(left, right) + 1

        dfs(root)
        return res

    def isBalancedIterative(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        height = {None: 0}
        stack = [root]

        while stack:
            curr = stack[-1]
            # peak at last element in stack

            if curr.left and curr.left not in height:
                stack.append(curr.left)
            elif curr.right and curr.right not in height:
                stack.append(curr.right)
            else:
                curr = stack.pop()
                leftHeight = height[curr.left]
                rightHeight = height[curr.right]

                if abs(leftHeight - rightHeight) > 1:
                    return False

                height[curr] = max(leftHeight, rightHeight) + 1
        return True


"""
Test Case:
root = [1,2,3,null,null,4] -> true
root = [1,2,3,null,null,4,null,5] -> false
root = [] -> true


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
If the difference in height between left and right children node is 1 than balanced

Visting each node takes O(n) and saving the height takes O(n)
"""