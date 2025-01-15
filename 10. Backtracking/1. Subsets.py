class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(nums, path, index):
            nonlocal res

            if index >= len(nums):
                res.append(path)
                return

            backtrack(nums, path, index + 1)
            backtrack(nums, path + [nums[index]], index + 1)

        backtrack(nums, [], 0)
        return res

"""
Test Case:
nums = [1,2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

"""

"""
Time Complexity: O(n*2^n) n steps and each step has 2 options (2^n) subsets
Space Complexity: O(n) - space grows linearly
"""

"""
Approach:
Start at first index, one path includes the current index in a subset and the other doesn't
Repeat for the next index
At the last index, append the subset to result
"""