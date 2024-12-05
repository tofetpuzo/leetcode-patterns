# 110. Balanced Binary Tree
# Easy
# Topics
# Companies
# Given a binary tree, determine if it is
# height-balanced
# .

# Example 1:

# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: true
# Example 2:


# Input: root = [1, 2, 2, 3, 3, null, null, 4, 4]
# Output: false
# Example 3:

# Input: root = []
# Output: true

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def is_balanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def check(root):
            if root is None:
                return 0

            left = check(root.left)
            right = check(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return check(root) != -1
