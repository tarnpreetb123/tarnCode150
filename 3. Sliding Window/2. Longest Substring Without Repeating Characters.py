class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        seen = []

        for i in s:
            while i in seen:
                seen.pop(0)
            seen.append(i)
            length = max(length, len(seen))
        return length

"""
Test Case
s = "zxyzxyz" => output = 3
"xxxx" -> output = 1
"abcbde" -> 4
"""
solution = Solution()
print(solution.lengthOfLongestSubstring("zxyzxyz"))
print(solution.lengthOfLongestSubstring("xxxx"))
print(solution.lengthOfLongestSubstring("pwwkew"))
print(solution.lengthOfLongestSubstring("aab"))
print(solution.lengthOfLongestSubstring("dvdf"))
print(solution.lengthOfLongestSubstring("abcbde"))

"""
Time Complexity: O(n)
Space Complexity: O(m) -> where m is the longest substring 
"""

"""
Approach:

"""
