# 101. Symmetric Tree
# Easy
# Topics
# Companies
# Given the root of a binary tree, check whether it is a mirror of itself(i.e., symmetric around its center).


# Example 1:


# Input: root = [1, 2, 2, 3, 4, 4, 3]
# Output: true
# Example 2:


# Input: root = [1, 2, 2, null, 3, null, 3]
# Output: false


# Constraints:

# The number of nodes in the tree is in the range[1, 1000].
# -100 <= Node.val <= 100


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def is_mirror(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False

            return (left.val == right.val) and is_mirror(left.right, right.left) and is_mirror(left.left, right.right)

        return is_mirror(root, root)
