class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if goal - i <= nums[i]:
                goal = i

        if goal == 0:
            return True
        else:
            return False

"""
Test Case:
nums = [1,2,0,1,0] -> true

"""

"""
Time Complexity: O(n) -> loop through array
Space Complexity: O(1) -> 1 variable
"""