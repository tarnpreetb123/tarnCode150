# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head

        while current:
            stack.append(current)
            current = current.next

        if stack:
            current = stack.pop()
        res = current
        while stack:
            prev = stack.pop()
            current.next = prev
            current = prev

        if current:
            current.next = None
        return res

    def reverse2(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

"""
Test Case
head = [0,1,2,3] => [3,2,1,0]

"""

head = ListNode(val=0)
second = ListNode(val=1)
third = ListNode(val=2)
fourth = ListNode(val=3)
head.next = second
second.next = third
third.next = fourth

solution = Solution()
# print(solution.reverseList(head).val)
print(solution.reverse2(head).val)

"""
Time Complexity: O(n) 
Space Complexity: O(n) -> second method is O(1)
"""

"""
Approach:

Insert linked-list into stack
Pop stack and make linked-list -> reversed

Better approach:

For each element in linked list,
make the prev element the next element and 
make the current element the new prev element
make the next element the new current element


(None) - [1] - 2 - 3 - 4 - None
(1) - None
[2] - 3 - 4 

(2) - 1 - None
[3] - 4

(3) - 2 - 1 - None
[4]

(4) - 3 - 2 - 1 - None
[None]

return prev == (4)

"""
