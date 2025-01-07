# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Traverse tree, BFS
        # For each node, gonna save the maximum value along the path
        # If maximum is greater than current node than that node is not good

        # Base case if root is none return 0
        if not root:
            return 0

        res = 0
        queue = deque([(root, -float('inf'))])

        while queue:
            curr, maxVal = queue.popleft()
            print(curr.val, maxVal)
            if curr.val >= maxVal:
                res += 1

            if curr.left:
                queue.append((curr.left, max(maxVal, curr.val)))
            if curr.right:
                queue.append((curr.right, max(maxVal, curr.val)))

        return res

"""
Test Case:
root = [2,1,1,3,null,1,5] -> 3
root = [1,2,-1,3,4] -> 4

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
Visit each node and for each node save the maximum value of parent nodes, in my solution I do bfs
If the current node's value is greater than maximum value of parents it is a good node and can be counted as such
"""