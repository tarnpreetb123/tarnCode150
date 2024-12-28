# Definition for singly-linked list.
from typing import Optional


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        curr = head
        curr2 = head
        prev = None
        while curr and curr2:
            prev = curr
            curr = curr.next
            curr2 = curr2.next
            if curr2:
                curr2 = curr2.next

        prev.next = None
        # print_linked_list(curr)
        # print_linked_list(head)

        curr2 = curr
        curr = head
        dummy = res = ListNode()
        prev = None

        while curr2:
            temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = temp

        curr2 = prev

        flip = True
        while curr and curr2:
            if flip:
                res.next = curr
                curr = curr.next
            else:
                res.next = curr2
                curr2 = curr2.next
            flip = not flip
            res = res.next

        if curr:
            res.next = curr
        elif curr2:
            res.next = curr2

        # print_linked_list(dummy.next)
        return None
"""
Test Case
list1 = [1,2,4], list2 = [1,3,5] => output = [1,1,2,3,4,5]
list 1 = [], list2 = [1] => output = [1]
"""

head = ListNode(val=0)
second = ListNode(val=1)
third = ListNode(val=2)
fourth = ListNode(val=3)
head.next = second
second.next = third
third.next = fourth

head2 = ListNode(val=2)
second2 = ListNode(val=4)
third2 = ListNode(val=6)
fourth2 = ListNode(val=8)
head2.next = second2
second2.next = third2
third2.next = fourth2

head3 = ListNode(val=0)
head3.next = ListNode(val=1)
head3.next.next = ListNode(val=2)
head3.next.next.next = ListNode(val=3)
head3.next.next.next.next = ListNode(val=4)
head3.next.next.next.next.next = ListNode(val=5)
head3.next.next.next.next.next.next = ListNode(val=6)

solution = Solution()
# print_linked_list(solution.reorderList(head))
# print_linked_list(solution.reorderList(head2))
print_linked_list(solution.reorderList(head3))

"""
Time Complexity:  O(n) -> 3n which reduces to n
Space Complexity: O(1)
"""

"""
Approach:

1: Add all elements in list to an array, take from the start and end of array to make final list
    Alternating between start and end

2: 



0 - 1 - 2 - 3 - 4 - 5 - 6
0 - 1 - 2 - 3 
 3 - 4 - 5 - 6 => 6 - 5 - 4 - 3

0 - 6 - 1 - 5 - 2 - 4 - 3


Slow and fast approach only need to check if fast and fast.next exist since it will terminate before slow
  
"""
