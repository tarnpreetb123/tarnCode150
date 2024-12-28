import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        leftPointer = 1
        rightPointer = max(piles)
        res = rightPointer

        while leftPointer <= rightPointer:
            k = leftPointer + (rightPointer - leftPointer)//2
            hours = 0
            for i in piles:
                hours += math.ceil(i/k)

            if hours > h:
                leftPointer = k + 1
            elif hours <= h:
                res = k
                rightPointer = k -1

        return res



"""
Test Case
piles = [1,4,3,2], h = 9, output => 2

"""
solution = Solution()
print(solution.minEatingSpeed([1, 4, 3, 2], 9))

"""
Time Complexity: O(log(m) * n) where m is the amount of bananas, n is piles
Space Complexity: O(1)
"""

"""
Approach:

Binary Search

Slowest rate is k=1 max rate would be k=piles(max)...binary search between them as long as the k works

"""
