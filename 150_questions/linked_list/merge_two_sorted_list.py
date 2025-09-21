# Description
# Editorial
# Editorial
# Solutions
# Solutions
# Submissions
# Submissions


# Code
# Testcase
# Test Result
# Test Result
# 21. Merge Two Sorted Lists
# Solved
# Easy
# Topics
# conpanies icon
# Companies
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Definition for singly-linked list.
from multiprocessing import dummy
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
           
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode(0)
        current = dummy
        
        # Pointers for both lists
        p1, p2 = list1, list2
        
        # Traverse both lists and append the smaller value to the merged list
        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        # If there are remaining nodes in either list, append them
        if p1:
            current.next = p1
        elif p2:
            current.next = p2
        
        # Return the merged list, which starts from the next of the dummy node
        return dummy.next
    
    
# Example usage:
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)# This will create a merged linked list: 1 -> 1 -> 2 -> 3 -> 4 -> 4
# Function to print the linked list
def print_linked_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
# print_linked_list(merged_list)# This will create a merged linked list: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None


print_linked_list(merged_list)


# doing it like I understand it
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        
        # 