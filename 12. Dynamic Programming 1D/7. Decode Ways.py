class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and s[i] != "0" and int(s[i:i + 2]) <= 26:
                dp[i] += dp[i + 2]

        return dp[0]
    def numDecodings2(self, s: str) -> int:
        stepOne = 1
        stepTwo = 1
        res = stepOne
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                res = 0
            else:
                res = stepOne
            if i + 1 < len(s) and s[i] != "0" and int(s[i:i + 2]) <= 26:
                res += stepTwo

            stepTwo = stepOne
            stepOne = res

        return res

"""
Test Case:
s = "12" -> 2

"""

"""
Time Complexity: O(n) -> loop through n chars
Space Complexity: O(n) -> we store an array for each sub char 

Second solution: Space Complexity: O(1) -> we use only 3 variables
"""


"""
Approach:

Start from the end of the string and decode s[i+1:] 
If the string is a '0' there are 0 ways to decode it

If the string is non '0' it can be decoded the same number of ways as i+1

If we consider a 2 digit decode only possible if the value is between 10-26 then
the decode ways is i+1 plus however many decodes happened before that at i+2

1012 -> decode "" -> 1
101 -> decode "2" -> 1
10 -> decode "1" & "2" -> 1
      decode "12" -> which makes the total decodes 1 plus 1 = 2
1 -> decode "0" & "12" -> 0 since "0" can not be a leading value
  -> decode "1" & "0" & "12" -> 0 since we established that "0" can not be alone
  -> decode "10" & "12" -> this can be decoded 0 plus 2, ssince "12" can be decoded 2 ways
  
end result "10" & "1" & "2" or "10" & "12"
1111 -> decode "" -> 1
111  -> decode "1" -> 1
11   -> decode "1" & "1" -> 1
        decode "11" -> 1 plus 1 = 2
1    -> decode "1" & "11" -> 2 ( we can have the "1" and the "11" or "1" and "1" and "1")
        decode "11" & "1" -> 2 plus 1 = 3 -> the plus 1 comes from "1" being decoded 1 way
""   -> decode "1" & "111" -> 3
        decode "11" & "11" -> 3 plus 2 = 5 -> the plus 2 comes from "11" being decoded 2 ways

We essentially just need too keep track of 2 values, the previous decoding of the subarray and the previous previous decoding amounts
"""