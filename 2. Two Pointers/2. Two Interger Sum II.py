class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        leftPointer = 0
        rightPointer = len(numbers) - 1

        while numbers[leftPointer] + numbers[rightPointer] != target:
            total = numbers[leftPointer] + numbers[rightPointer]

            if total > target:
                rightPointer -= 1
            if total < target:
                leftPointer += 1

        return [leftPointer+1, rightPointer+1]

"""
Test Case
numbers = [1,2,3,4], target = 3 => result: [1,2]
numers = [1,2,3,4,6], target = 6 => result: [2,4]

"""
solution = Solution()
print(solution.twoSum([1, 2, 3, 4], 3))
print(solution.twoSum([3, 4, 5, 6], 7))
print(solution.twoSum([2, 5, 5, 11], 10))
print(solution.twoSum([1,2,3,4,6], 6))

"""
Time Complexity: O(n)
Space Complexity: O(1) -> enforced 
"""

"""
Approach:
Start at both ends of array and check if the solution matches
If the sum is too high, reduce it and if too low, increase it
"""
