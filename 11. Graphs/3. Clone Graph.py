"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        queue = deque()
        res = None
        clones = {}

        if node:
            res = Node(node.val)
            clones[node.val] = res
            queue.append(node)

        while queue:
            curr = queue.popleft()
            newNeighbors = []

            for n in curr.neighbors:

                if n.val not in clones:
                    queue.append(n)
                    clones[n.val] = Node(n.val)

                newNeighbors.append(clones[n.val])

            clones[curr.val].neighbors = newNeighbors

        return res

"""
Test Case:
Input: adjList = [[2],[1,3],[2]]

Output: [[2],[1,3],[2]]
"""

"""
Time Complexity: O(V + E) -> V is nodes, E is edges
Space Complexity: O(V) -> copying each node, only storing nodes linearly
"""

"""
Approach:
Start with first node
For each node, copy is a copy doesn't exist, goo through neighbours, copy each neighbour if it doesn't exist
Update nodes neighbours
"""