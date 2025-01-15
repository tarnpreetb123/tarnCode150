import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k

        heapq.heapify(self.minHeap)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]

"""
Test Case:
["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]] -> [null,3,3,3,5,6]

"""

"""
Time Complexity: mlog(n) -> mlog(k)  --- m is the number of inserts
Space Complexity: O(n) -> O(k)
"""

"""
Approach:
Keep a min heap of size k, the kth largest element is the minimum of the resulting k elements in the minheap

Adding, insert the value into the minHeap and make sure minHeap stays as big as k
"""