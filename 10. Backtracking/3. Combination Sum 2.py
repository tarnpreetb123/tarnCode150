class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def combination(nums, path):

            total = sum(path)

            if total > target:
                return
            elif total == target:
                res.append(path)
                return

            i = 0
            while i < len(nums):
                combination(nums[i + 1:], path + [nums[i]])
                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1

                i += 1

        combination(candidates, [])
        return res


"""
Test Case:
Input: candidates = [9,2,2,4,6,1,5], target = 8

Output: [
  [1,2,5],
  [2,2,4],
  [2,6]
]


"""

"""
Time Complexity: O(n* 2^n) -> O(n) while loop and the backtracking call grows by 2^n
Space Complexity: O(n)
"""

"""
Approach:
Start at first index, add to path, every other num from the current index to end is valid, recursively add next num
In our loop of calling, skip the same index
If we total is higher than target, path is invalid, if total is target, path is valid

1,2,2,4 -> 1 -> 2 -> 2...
2,2,4 -> 2 -> 4 ...
4 -> 4 ... We have skipped the second two
"""