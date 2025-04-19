class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        sumGas = 0
        index = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            sumGas += diff

            if sumGas < 0:
                sumGas = 0
                index = i + 1

        return index


"""
Test Case:
Input: gas = [1,2,3,4], cost = [2,2,4,1]
Output: 3

"""

"""
Time Complexity: O(n) -> loop through array
Space Complexity: O(1) -> 2 variable
"""