class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            stepOne = 0
            stepTwo = 0

            for i in nums:
                maxSoFar = max(i + stepOne, stepTwo)
                stepOne = stepTwo
                stepTwo = maxSoFar

            return stepTwo

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

"""
Test Case:
nums = [2,9,8,3,6] -> 15

"""

"""
Time Complexity: O(n) -> O(n) looping from n down to 0
Space Complexity: O(1) -> 2 variables
"""

"""
Approach:

DP approach, at each n house, compute the maxRobbed as going down the street
Either we rob the nth house which means we can rob up to n-2 hours plus n
or we don't rob the nth house which means we can rob up to n-1 and have to skip n


Given that the houses are circular, if we include the first element then the last element can't be used
If using the second element than the first element can not be used
The max of either of those is the ans
Special case: if only one element

[2,9,8,3,6]

Run it on:
[2,9,8,3] & [9,8,3,6] & [2] the max out of those 3 options is the result
"""