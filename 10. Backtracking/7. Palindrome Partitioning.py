class Solution:

    def isPalidrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:

        res = []

        def dfs(s, i, part):

            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalidrome(s, i, j):
                    part.append(s[i: j + 1])
                    dfs(s, j + 1, part)
                    part.pop()

        dfs(s, 0, [])

        return res

"""
Test Case:
Input: s = "aab"

Output: [["a","a","b"],["aa","b"]]

"""

"""
Time Complexity: O(n* 2^n) -> we go through n letters in the input and for each letter we can split or not split hench 2^n
Space Complexity: O(n) -> 
"""

"""
Approach:
For every index of the palindrome, split or not split. If splitting, continue onwards splitting or not splitting
Essentially at each index we split the array and if we arrive at the end with only palindromes then it was a valid solution otherwise backtrack

aab -> a, aa, aab
a -> a or ab ... ab is invalid ... a->b resulting in a->a->b
aa -> b result aa->b
aab -> invalid 
"""