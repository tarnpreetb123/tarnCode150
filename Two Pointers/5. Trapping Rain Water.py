class Solution:
    def trap(self, height: list[int]) -> int:

        leftPointer = 0
        rightPointer = 1
        waterArea = 0
        flag = True
        waterFlag = True
        while rightPointer < len(height):
            # print(f"water: {waterArea}, left: {leftPointer}, right: {rightPointer}")
            flag = True
            waterFlag = True
            currentWater = 0
            # if height[leftPointer] > 0 and height[rightPointer] > 0:
            # print(f"water: {waterArea}, left: {leftPointer}, right: {rightPointer}")
            if rightPointer > leftPointer:
                checkPointer = rightPointer - 1
                maxHeight = max(height[leftPointer], height[rightPointer])
                minHeight = min(height[leftPointer], height[rightPointer])
                while checkPointer > leftPointer:
                    if rightPointer < len(height) - 1:
                        if height[rightPointer + 1] > height[rightPointer]:
                            # print(f"height1: {height[rightPointer+1]} ")
                            waterFlag = False
                    if height[checkPointer] >= maxHeight:
                        leftPointer += 1
                        flag = False
                        break
                    elif height[checkPointer] < minHeight:
                        currentWater += minHeight - height[checkPointer]
                        # print(minHeight, height[checkPointer])
                    checkPointer -= 1

            if waterFlag:
                waterArea += currentWater

            if flag:
                rightPointer += 1

            # print(f"water: {waterArea}, left: {leftPointer}, right: {rightPointer}")

        return waterArea

"""
Test Case
height = [0,2,0,3,1,0,1,3,2,1] => output = 9
"""
solution = Solution()
print(solution.trap([0,2,0,3,1,0,1,3,2,1]))

"""
Time Complexity: 
Space Complexity: 
"""

"""
Approach:
Both pointers start at value 0
Check how much water can be stored between left and right pointer 
If right > left and no other heights between them are bigger
Then compute current water level given the smaller height

If there is a bigger height then update left pointer, otherwise update right pointer

"""
