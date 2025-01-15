import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        freq = [0] * 26

        for i in tasks:
            freq[ord(i) - ord('A')] -= 1

        freq = [i for i in freq if i != 0]

        heapq.heapify(freq)
        queue = deque()
        time = 0

        while freq or queue:
            time += 1
            if freq:
                cnt = heapq.heappop(freq) + 1

                if cnt:
                    queue.append([cnt, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(freq, queue.popleft()[0])
        return time


solution = Solution()
print(solution.leastInterval(["X", "X", "Y", "Y"], 2))

"""
Test Case:
["X", "X", "Y", "Y"], 2 -> 5

"""

"""
Time Complexity: O(n)*N big n is the idle time
Space Complexity: O(1) 26 total elements constant
"""

"""
Approach:
Count how many of each character there is, remove the 0's, use a max heap
The most freq char is used up first and then put into a queue to wait out idle time
One the idle time is finished inserted back into the max heap
"""