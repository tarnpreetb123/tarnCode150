class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        buckets = {}

        for strings in strs:
            freq = [0]*26
            for char in strings:
                freq[ord(char) - ord('a')] += 1
            index = ".".join(str(i) for i in freq)
            buckets[index] = buckets.get(index, []) + [strings]

        return list(buckets.values())

"""
Test Case
["act","pots","tops","cat","stop","hat"]

Result:
[["hat"],["act", "cat"],["stop", "pots", "tops"]]

"""
solution = Solution()
print(solution.groupAnagrams(["acct","pots","tops","cat","stop","hat"]))
print(solution.groupAnagrams(["x"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"]))

"""
Time Complexity: O(n * m) where n is number of strings and m is number of chars
Space Complexity:  O(n) where n is number of strings
"""

"""
Approach:

Check the frequency of each string with all other strings, if they match then it's a group
"""