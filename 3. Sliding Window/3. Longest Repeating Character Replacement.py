class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = []
        length = 0
        freq = [0]*26

        for i in s:

            replacements = len(window) - max(freq)
            while replacements > k:
                # print(window, replacements, length)
                letter = window.pop(0)
                # print(window, replacements, letter, length)
                freq[ord(letter) - ord('A')] -= 1
                replacements = len(window) - max(freq)

            window.append(i)
            freq[ord(i) - ord('A')] += 1
            replacements = len(window) - max(freq)
            if replacements <= k:
                length = max(length, len(window))

        return length


"""
Test Case
s = "XYYX", k = 2 => output = 4
s = "AAABABB", k = 1 => output = 5
s = "ABABBBC
"""
solution = Solution()
print(solution.characterReplacement("XYYX", 2))
print(solution.characterReplacement("AAABABB", 1))

"""
Time Complexity: O(n)
Space Complexity: O(m) -> substring length
"""

"""
Approach:

"""
