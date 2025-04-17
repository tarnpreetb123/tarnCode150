class Solution:
    def climbStairs(self, n: int) -> int:

        res = 0

        def climb(currN):
            nonlocal res
            if currN == n:
                res += 1
            if currN > n:
                return
            else:
                climb(currN + 1)
                climb(currN + 2)

        climb(0)
        return res

    def climbStairs2(self, n: int) -> int:
        oneStep = 1
        twoStep = 1
        res = 1

        for i in range(n - 1):
            res = oneStep + twoStep
            twoStep = oneStep
            oneStep = res

        return res
"""
Test Case:
Input: n = 5  -> 8

"""

"""
Time Complexity: O(n) -> O(n) looping from n down to 0
Space Complexity: O(1) -> 2 variables
"""

"""
Approach:
DP Bottom up approach, each step compute the number of ways to get to get res
Start at n and n-1, compute n-2 which is the sum of n and n-1, shift reach variable by one
[0, 1, 2, 3, 4, 5]
[.,.,.,.,1,1] -> [.,.,.,2,1,1] -> [.,.,3,2,1,1]
It's essentially computing the fib sequence
"""