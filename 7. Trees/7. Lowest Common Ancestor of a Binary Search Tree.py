# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        stack = deque([root])
        lca = root

        while stack:
            curr = stack.pop()

            if curr.val > p.val and curr.val > q.val:
                stack.append(curr.left)
            elif curr.val < p.val and curr.val < q.val:
                stack.append(curr.right)
            else:
                lca = curr
        return lca


"""
Test Case:
root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8 -> 5
root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4 -> 3
root = [] -> true


"""

"""
Iterative
Time Complexity: O(h)
Space Complexity: O(1)


DFS
Time Complexity: O(h) 
Space Complexity: O(h) -> h is height of tree
"""

"""
Approach:
Visit each node, if the two given nodes are both greater than or both less than our visited node proceed down left or right children 
else the visited node is our least common ancestor, this is due to the fact that it's a binary search tree, the lca must
be between the two given nodes and not outside of that range.
"""