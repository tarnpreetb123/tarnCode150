class Solution:
    def trap(self, height: list[int]) -> int:

        leftPointer = 0
        rightPointer = len(height) - 1

        leftMax = height[leftPointer]
        rightMax = height[rightPointer]

        water = 0

        while leftPointer < rightPointer:

            if leftMax < rightMax:
                leftPointer += 1
                leftMax = max(leftMax, height[leftPointer])
                water += leftMax - height[leftPointer]
            else:
                rightPointer -= 1
                rightMax = max(rightMax, height[rightPointer])
                water += rightMax - height[rightPointer]

        return water


"""
Test Case
height = [0,2,0,3,1,0,1,3,2,1] => output = 9
"""
solution = Solution()
print(solution.trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
Approach:
The water for a given index is equal to the minimum of the maximum left and max right values
minus the height at the given index


Improvements using 2 points
Start a pointer on either end
While left < right
If maxLeft < maxRight operate on left else operate on right
Update Pointer and take max between new index and old max
The difference between max and index is water to be added to res
"""
