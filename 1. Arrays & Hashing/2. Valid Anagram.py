class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwyxz"
        hashMap = {}

        for letter in alphabet:
            hashMap[letter] = 0

        for char in s:
            hashMap[char] += 1
        for char in t:
            hashMap[char] -= 1

        for x in hashMap:
            if hashMap[x] != 0:
                return False
        return True

"""
Test Case 1
'ace' and 'race' not anagrams since r is extra but all of ace is inside race
'acer' and 'race' are anagrams
'jam' and 'jim' are not anagrams
"""

solution = Solution()
print(solution.isAnagram('racecar', 'carrace'))

"""
Time Complexity: 
Space Complexity:
"""