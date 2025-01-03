# 19. Remove Nth Node From End of List
# Medium
# Topics
# Companies
# Hint
# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:


# Input: head = [1, 2, 3, 4, 5], n = 2
# Output: [1, 2, 3, 5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1, 2], n = 1
# Output: [1]


# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Follow up: Could you do this in one pass ?


def removeNthFromEnd(head, n):
    """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    for i in range(n + 1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next

# Time complexity: O(n)
# Space complexity: O(1)
