import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        maxHeap = []

        for i in stones:
            heapq.heappush(maxHeap, -i)  # push negative values, the min value is the max value

        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x > y:
                x = x - y
                heapq.heappush(maxHeap, -x)

        if len(maxHeap):
            return -maxHeap[0]
        else:
            return 0

"""
Test Case:
stones = [2,3,6,2,4] -> 1

Explanation:
We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
We smash 2 and 2, so the array becomes [1].

"""

"""
Time Complexity: nlog(n), n steps taken with each step taking log(n) time
Space Complexity: O(n)
"""

"""
Approach:
Keep a max heap by storing the negatives of the positive results, each round take the two smallest(biggest) values
from the max heap and calculate, insert the result back into the max heap, continue until 1 result
"""