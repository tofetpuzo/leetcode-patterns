# 23. Merge k Sorted Lists
# Hard
# Topics
# Companies
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:

# Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# Output: [1, 1, 2, 3, 4, 4, 5, 6]
# Explanation: The linked-lists are:
# [
#     1 -> 4 -> 5,
#     1 -> 3 -> 4,
#     2 -> 6
# ]
# merging them into one sorted list:
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
# Definition for singly-linked list.
from heapq import heappush, heappop


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
    """
    heap = []
    for i, node in enumerate(lists):
        if node:
            heappush(heap, (node.val, i, node))

    dummy = ListNode()
    curr = dummy

    while heap:
        _, i, node = heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heappush(heap, (node.next.val, i, node.next))

    return dummy.next
