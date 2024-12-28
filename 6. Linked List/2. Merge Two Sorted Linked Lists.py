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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        res = None

        if curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                res = curr1
                curr1 = curr1.next
            else:
                res = curr2
                curr2 = curr2.next

        elif curr1 is not None:
            res = curr1
            curr1 = curr1.next
        elif curr2 is not None:
            res = curr2
            curr2 = curr2.next
        finalHead = res

        while curr1 is not None or curr2 is not None:

            if curr1 is not None and curr2 is not None:
                if curr1.val < curr2.val:
                    res.next = curr1
                    curr1 = curr1.next
                else:
                    res.next = curr2
                    curr2 = curr2.next
            elif curr1 is not None:
                res.next = curr1
                curr1 = curr1.next
            elif curr2 is not None:
                res.next = curr2
                curr2 = curr2.next
            res = res.next
        return finalHead


"""
Test Case
list1 = [1,2,4], list2 = [1,3,5] => output = [1,1,2,3,4,5]
list 1 = [], list2 = [1] => output = [1]
"""

head = ListNode(val=0)
second = ListNode(val=1)
third = ListNode(val=12)
fourth = ListNode(val=13)
head.next = second
second.next = third
third.next = fourth

head2 = ListNode(val=0)
second2 = ListNode(val=10)
third2 = ListNode(val=42)
head2.next = second2
second2.next = third2

solution = Solution()
print_linked_list(solution.mergeTwoLists(head, head2))

"""
Time Complexity:  O(n + m) -> linear time n and m are the lengths of the two lists
Space Complexity: O(1)
"""

"""
Approach:
Loop while we have elements in either list
Select the lower of the two elements to be inserted into result
By selecting the lowest element everytime the new list will remain sorted

"""
