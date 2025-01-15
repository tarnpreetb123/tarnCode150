import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])

            while len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []

        while len(maxHeap):
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])

        return res


"""
Test Case:
points = [[0,2],[2,0],[2,2]], k = 2 -> [[0,2],[2,0]]

"""

"""
Time Complexity: nlog(k), n steps taken with each step taking log(k) time, n steps cuz n inserts each insert takes log(k)
Space Complexity: O(k)
"""

"""
Approach:
Keep a max heap by storing the negatives of the positive distances, keep the maxHeap only k elements long and
then return all elements
"""