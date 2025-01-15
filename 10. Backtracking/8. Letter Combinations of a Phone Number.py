class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hashMap = {"2": ["a", "b", "c"],
                   "3": ["d", "e", "f"],
                   "4": ["g", "h", "i"],
                   "5": ["j", "k", "l"],
                   "6": ["m", "n", "o"],
                   "7": ["p", "q", "r", "s"],
                   "8": ["t", "u", "v"],
                   "9": ["w", "x", "y", "z"]}

        def dfs(index, sol):

            if index >= len(digits):
                if sol != "":
                    res.append(sol)
                return

            curr = hashMap[digits[index]]

            for i in curr:
                sol += i
                dfs(index + 1, sol)
                sol = sol[:-1]

        dfs(0, "")

        return res

"""
Test Case:
Input: digits = "34"

Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]

"""

"""
Time Complexity: O(n* 4^n) -> we go through n letters in the input and for each letter we have 4 options hence 4^n
Space Complexity: O(n) 
"""

"""
Approach:
For every digit, go through all letters and dfs down the graph, if the graph ends then the base case takes over the the sol is added to results

"""