class Solution:
    def search(self, nums: list[int], target: int) -> int:

        leftPointer = 0
        rightPointer = len(nums) - 1
        res = -1

        if leftPointer == rightPointer:
            if nums[leftPointer] == target:
                res = leftPointer

        while leftPointer < rightPointer:
            midPointer = int((rightPointer + leftPointer)/2)
            # print(leftPointer, midPointer, rightPointer)
            # print(nums, nums[midPointer], target)

            if nums[midPointer] < target:
                leftPointer = midPointer+1
            else:
                rightPointer = midPointer

            midPointer = int((rightPointer + leftPointer) / 2)
            if nums[midPointer] == target:
                res = midPointer
                break

        return res


"""
Test Case
[-1,0,2,4,6,8], 4 => 3, outputs index of target

"""
solution = Solution()
print(solution.search([-1, 0, 2, 4, 6, 8], 3))
print(solution.search([-1, 0, 2, 4, 6, 8], 8))
print(solution.search([2,5], 5))
print(solution.search([5], 5))

"""
Time Complexity: O(logn)
Space Complexity: 
"""

"""
Approach:
Binary Search
"""
