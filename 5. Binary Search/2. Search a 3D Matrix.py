class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        result = False
        leftOutter = 0
        rightOutter = len(matrix) - 1
        leftInner = 0
        rightInner = len(matrix[0]) - 1
        listIndex = -1

        while leftInner <= rightInner:

            while leftOutter <= rightOutter:
                midOutter = leftOutter + (rightOutter - leftOutter) // 2
                if matrix[midOutter][0] > target:
                    rightOutter = midOutter - 1
                elif matrix[midOutter][-1] < target:
                    leftOutter = midOutter + 1
                else:
                    listIndex = midOutter
                    rightOutter = leftOutter - 1

            if listIndex < 0:
                break

            midInner = leftInner + (rightInner - leftInner) // 2
            if matrix[listIndex][midInner] > target:
                rightInner = midInner - 1
            elif matrix[listIndex][midInner] < target:
                leftInner = midInner + 1
            else:
                result = True
                break

        return result


"""
Test Case
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10 => true
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15 => false

"""
solution = Solution()
print(solution.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10))
print(solution.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15))
print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

"""
Time Complexity: O(log(m*n)) = O(logm + logn)
Space Complexity: 
"""

"""
Approach:

Make 2 binary searches, one to go through the lists using the first and last element and then a second within that 


"""
