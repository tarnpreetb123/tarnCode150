class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        result = False
        for num in nums:
            if num in seen:
                result = True
            else:
                seen.add(num)
        return result

    def hasDuplicate2(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)

"""
Test Cases
'1,2,3,4,5,6,7,8,9,10' no duplicates
'1,2,3,3,5,6,7,8,9,10' duplicates
"""

solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution.hasDuplicate([1, 2, 3, 3, 5, 6, 7, 8, 9, 10]))
print(solution.hasDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution.hasDuplicate([1, 2, 3, 4, 4, 6, 7, 8, 9, 10]))

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""