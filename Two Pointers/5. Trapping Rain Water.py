class Solution:
    def trap(self, height: list[int]) -> int:

        maxLeft = []
        maxRight = []
        maxVal = 0
        water = 0

        for i in range(len(height)):
            maxVal = max(maxVal, height[i])
            maxLeft.append(maxVal)
        maxVal = 0

        for i in range(len(height) - 1, -1, -1):
            maxVal = max(maxVal, height[i])
            maxRight.insert(0, maxVal)

        print(maxLeft)
        print(maxRight)

        for i in range(len(height)):
            water += min(maxLeft[i], maxRight[i]) - height[i]
        return water



"""
Test Case
height = [0,2,0,3,1,0,1,3,2,1] => output = 9
"""
solution = Solution()
print(solution.trap([0,2,0,3,1,0,1,3,2,1]))

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

"""
Approach:
The water for a given index is equal to the minimum of the maximum left and max right values
minus the height at the given index

"""
