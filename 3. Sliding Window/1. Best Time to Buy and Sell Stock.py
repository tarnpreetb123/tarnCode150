class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        minPrice = prices[0]
        sellPrice = 0
        for i in prices:
            minPrice = min(minPrice, i)
            sellPrice = max(sellPrice, i - minPrice)
        return sellPrice

"""
Test Case
prices = [10,1,5,6,7,1] => output = 6
[10,8,7,5,2] -> output = 0
"""
solution = Solution()
print(solution.maxProfit([10,1,5,6,7,1]))
print(solution.maxProfit([10,8,7,5,2]))

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
Approach:

Loop through the prices, at index i is the price we sell at
Find the minimum price to the left of i and check profit
"""
