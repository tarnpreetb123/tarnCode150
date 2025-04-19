class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currSum = 0


        for i in nums:
            if currSum < 0:
                currSum = 0

            currSum += i
            res = max(res, currSum)


        return res

    def maxSubArray2(self, nums):
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)

"""
Test Case:
nums = [2,-3,4,-2,2,1,-1,4] -> 8

"""

"""
Time Complexity: O(n) -> loop through array
Space Complexity: O(1) -> saving 2 variables

Second solution: Space Complexity: O(n) -> dp cache
"""

"""
Approach:

The dp approach calculates the maximum subarray value at each index, the max value is either the current value itself,
starting a new subarray or the current value plus the previous max value in cache
"""