# 148. Sort List
# Solved
# Medium
# Topics
# conpanies icon
# Companies
# Given the head of a linked list, return the list after sorting it in ascending order.

 

# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105
 

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Step 1: Get the length of the list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0)
        dummy.next = head
        step = 1

        # Step 2: Bottom-up merge
        while step < length:
            prev = dummy
            curr = dummy.next

            while curr:
                # Step 3: Split the list into two halves of size 'step'
                left = curr
                right = self.split(left, step)
                curr = self.split(right, step)

                # Step 4: Merge and connect
                merged = self.merge(left, right)
                prev.next = merged[0]
                prev = merged[1]  # move to the tail of the merged sublist

            step *= 2

        return dummy.next

    # Split the list into two parts, first 'size' nodes and the rest
    def split(self, head, size):
        if not head:
            return None
        for i in range(size - 1):
            if head.next:
                head = head.next
            else:
                break
        rest = head.next
        head.next = None
        return rest

    # Merge two sorted lists and return head and tail of merged list
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2

        # Move tail to the end
        while tail.next:
            tail = tail.next

        return (dummy.next, tail)


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves
        slow, fast = head, head.next  # start fast one step ahead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None  # split the list

        # Step 2: Recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge the sorted halves
        return self.merge(left, right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach remaining nodes
        tail.next = l1 if l1 else l2

        return dummy.next
