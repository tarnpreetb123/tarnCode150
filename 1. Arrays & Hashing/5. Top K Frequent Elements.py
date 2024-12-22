class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        hashMap = {}
        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1

        topK = [[] for _ in range(len(nums)+1)]
        print(topK)
        for key in hashMap.keys():
            topK[hashMap[key]].append(key)

        result = []
        for i in range(len(topK)-1, 0, -1):
            for num in topK[i]:
                result.append(num)

                if len(result) == k:
                    return result

"""
Test Case
nums = [1,2,2,3,3,3], k = 2 -> result = [2,3]
nums = [7,7], k = 1 => result = [7]
nums = [7,7,8,8], k = 2

"""
solution = Solution()
print(solution.topKFrequent([1,2,2,3,3,3], 2))
print(solution.topKFrequent([7,7], 1))
print(solution.topKFrequent([7,7, 8], 2))
# print(solution.topKFrequent())

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

"""
Approach:
Count the frequency of each number in said array
Put each num and frequency into an array, sort pop out top k


A better approach is to instead make n buckets for frequencies 1 to n
Put each number into it's corresponding bucket
Pop out K buckets from list, it will be auto sorted
"""