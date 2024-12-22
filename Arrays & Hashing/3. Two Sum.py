class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], []) + [i]

        for i in range(len(nums)):
            missing = target - nums[i]
            if missing != nums[i] and missing in hashMap:
                return [i, hashMap[missing][0]]
            elif missing == nums[i] and missing in hashMap:
                if len(hashMap[missing]) > 1:
                    return [i, hashMap[missing][1]]
"""
Test Case
nums = [3,4,5,6], target = 7, result = [0,1]
nums = [2, 5, 5, 11], target = 10, result = [1, 2] -> same digit adds to target
nums = [1,3,4,2], target = 6, result = [2,3] -> smaller number second
Only 1 pair for output and smaller indice first

"""
solution = Solution()
print(solution.twoSum([3,4,5,6], 7))
print(solution.twoSum([2,5,5,11], 10))
print(solution.twoSum([1,3,4,2], 6))

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

"""
Improvements that can be made, single pass to check if num[i] is in hashMap
If it is then return [hashMap[target-num[i], i] otherwise add num[i] to hashMap
"""