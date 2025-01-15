import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]


"""
Test Case:
nums = [2,3,1,5,4], k = 2 -> 4

"""

"""
Time Complexity: nlog(k), n steps taken with each step taking log(k) time, n steps cuz n pops each pop takes log(k)
Space Complexity: O(k)
"""

"""
Approach:
Keep a min heap of size k, the minimum of that heap is the Kth largest Element in the array
"""