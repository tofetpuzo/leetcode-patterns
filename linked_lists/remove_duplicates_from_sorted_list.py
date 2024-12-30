# 83. Remove Duplicates from Sorted List
# Solved
# Easy
# Topics
# Companies
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.


# Example 1:


# Input: head = [1, 1, 2]
# Output: [1, 2]
# Example 2:


# Input: head = [1, 1, 2, 3, 3]
# Output: [1, 2, 3]


# Constraints:


# The number of nodes in the list is in the range[0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def delete_duplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
# Time complexity: O(n)
# Space complexity: O(1)
