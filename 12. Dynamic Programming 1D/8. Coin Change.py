class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            curRes = i
            for coin in coins:
                if curRes - coin > 0:
                    dp[curRes] = min(1 + dp[curRes - coin], dp[curRes])
                elif curRes - coin == 0:
                    dp[curRes] = 1  # curRes-coin = 0 -> dp[0] = 0 from the if portion

        res = dp[amount]
        if res == amount + 1:
            res = -1
        return res

"""
Test Case:
coins = [1,5,10], amount = 12

"""

"""
Time Complexity: O(n*t) -> n is length of coins and t is the amount -> n^2 ish
Space Complexity: O(t) -> we store an array as long as amount 
"""