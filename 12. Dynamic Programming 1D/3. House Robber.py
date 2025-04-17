class Solution:
    def rob(self, nums: List[int]) -> int:
        stepOne = 0
        stepTwo = 0

        for i in nums:
            maxSoFar = max(i + stepOne, stepTwo)
            stepOne = stepTwo
            stepTwo = maxSoFar
        return maxSoFar

"""
Test Case:
nums = [2,9,8,3,6] - > 16

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
"""