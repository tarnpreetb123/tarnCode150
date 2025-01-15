class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        def subset(nums, path, index):

            if index >= len(nums):
                res.append(path)
                return

            subset(nums, path + [nums[index]], index + 1)

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            subset(nums, path, index + 1)

        subset(nums, [], 0)
        return res

    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        def subset(nums, path):

            res.append(path)

            index = 0
            while index < len(nums):
                subset(nums[index + 1:], path + [nums[index]])
                while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                    index += 1

                index += 1

        subset(nums, [])
        return res



"""
Test Case:
Input: nums = [1,2,1] -> [[],[1],[1,2],[1,1],[1,2,1],[2]]

"""

"""
Time Complexity: O(n*2^n) -> O(n) for loop and O(2^n) growth oof subset tree
Space Complexity: O(2^n) -> 2^n subset tree size growth 
"""

"""
Approach:
Sort unique numbers, for each number, insert and don't insert into path, skip over duplicates when starting the chain

1,2,1 -> 1,1,2

First subcall on the 1
1,1,2 -> (1) 1,2 -> (1,1) 2 or (1,2) 1  we can either insert 1 or nothing on the second step
(1,1) 2 -> (1,1,2) 
(1, 2) 1 -> remains as is

Second subcall on the 2 since the second 1 is skipped
1,1,2 -> (2) 

1,2,3 -> (2) 1,3 -> (2,1) 3 -> (2,1,3) each time we select on number and add it to the permutations
"""