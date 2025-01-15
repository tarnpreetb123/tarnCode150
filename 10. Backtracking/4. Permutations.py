class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def per(nums, path):

            if not nums:
                res.append(path)
            for i in range(len(nums)):
                per(nums[:i] + nums[i + 1:], path + [nums[i]])

        per(nums, [])
        return res


"""
Test Case:
Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


"""

"""
Time Complexity: O(n*n!) -> O(n) for loop and O(n!) permutations
Space Complexity: O(n*n!) -> O(n!) permutations need to be saves, O(n) path length
"""

"""
Approach:
Start at first index, add to path, every other num is valid option for next step, keep going until all numbers used

1,2,3 -> (1) 2,3 -> (1,2) 3 -> (1,2,3)
1,2,3 -> (2) 1,3 -> (2,1) 3 -> (2,1,3) each time we select on number and add it to the permutations
"""