# 206. Reverse Linked List
# Easy
# Topics
# Companies
# Given the head of a singly linked list,
# reverse the list, and return the reversed list.


# Example 1:


# Input: head = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
# Example 2:


# Input: head = [1, 2]
# Output: [2, 1]
# Example 3:

# Input: head = []
# Output: []


# Constraints:

# The number of nodes in the list is the range[0, 5000].
# -5000 <= Node.val <= 5000


# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        before = None
        current = head
        while current:
            next_node = current.next
            current.next = before
            before = current
            current = next_node
        return before


# Time complexity: O(n)
# Space complexity: O(1)


# test case
head = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
# head = [1, 2]
# Output: [2, 1]


print(Solution().reverseList(head))  # [5, 4, 3, 2, 1]
