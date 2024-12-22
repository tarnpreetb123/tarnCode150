class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = ''.join(x for x in s if x.isalnum())
        pointerL = 0
        pointerR = len(s) - 1

        while pointerL <= pointerR:
            if s[pointerL] == s[pointerR]:
                pointerL += 1
                pointerR -= 1
            else:
                return False

        return True


"""
Test Case
"Was it a car or a cat I saw?" -> yes
"idk" -> no
"aba" -> yes
"""
solution = Solution()
print(solution.isPalindrome("Was it a car or a cat I saw?"))
print(solution.isPalindrome("idk"))
print(solution.isPalindrome("aba"))

"""
Time Complexity: O(n)
Space Complexity: O(1) 
"""

"""
Approach:
"""
