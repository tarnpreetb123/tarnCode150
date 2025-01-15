class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def combination(nums, path):

            total = sum(path)
            if total > target:
                return
            elif total == target:
                res.append(path)
            else:
                for i in range(len(nums)):
                    combination(nums[i:], path + [nums[i]])
        combination(nums, [])
        return res

    """
    Test Case:
    nums=[2,5,6,9], total=9 -> [[2,2,5],[9]]

    """

    """
    Time Complexity: O(2*t/m)
    Space Complexity: O(t/m) - t->target m-> minimum value in nums
    """

    """
    Approach:
    Start at first index, add to path, every other num from the current index to end is valid, recursively add next num
    If we total is higher than target, path is invalid, if total is target, path is valid
    
    2,5,6,9 (2) -> 2,5,6,9 (2) -> 2, 5, 6, 9 (5) = 9
    2,5,6,9 (9) -> [] = 9
    """
