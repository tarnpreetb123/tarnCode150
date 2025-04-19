class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        steps = 0

        while r < len(nums) - 1:
            maxIndex = 0
            for i in range(l, r + 1):
                maxIndex = max(maxIndex, nums[i] + i)

            l = r + 1
            r = maxIndex
            steps += 1

        return steps


"""
Test Case:
nums = [2,4,1,1,1,1] -> 2

"""

"""
Time Complexity: O(n) -> loop through array
Space Complexity: O(1) -> 2 variable
"""