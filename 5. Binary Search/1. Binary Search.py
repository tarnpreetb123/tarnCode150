class Solution:
    def search(self, nums: list[int], target: int) -> int:

        leftPointer = 0
        rightPointer = len(nums) - 1
        res = -1

        while leftPointer <= rightPointer:
            #(leftPointer + rightPointer)//2 might overflow if right and left add together higher than the underlying data type
            midPointer = leftPointer + ((rightPointer - leftPointer) // 2)

            if nums[midPointer] < target:
                leftPointer = midPointer + 1
            elif nums[midPointer] > target:
                rightPointer = midPointer - 1
            else:
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
Space Complexity: O(1)
"""

"""
Approach:
Binary Search, since the array is sorted look at the middle value and if target is less than or greater than we
can eliminate half the search domain
"""
