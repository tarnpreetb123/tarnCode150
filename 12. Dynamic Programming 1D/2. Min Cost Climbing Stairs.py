class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        res = 0
        stepOne = cost[-2]
        stepTwo = cost[-1]
        n = len(cost)
        for i in range(n-3, -1, -1):
            res = cost[i] + min(stepOne, stepTwo)
            stepTwo = stepOne
            stepOne = res

        return min(stepOne, stepTwo)

"""
Test Case:
Cost = [1,2,3]  -> 2

"""

"""
Time Complexity: O(n) -> O(n) looping from n down to 0
Space Complexity: O(1) -> 2 variables
"""