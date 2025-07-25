# 199. Binary Tree Right Side View
# Medium
# Topics
# conpanies icon
# Companies
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:

# Input: root = [1,2,3,null,5,null,4]

# Output: [1,3,4]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,null,null,null,5]

# Output: [1,3,4,5]

# Explanation:



# Example 3:

# Input: root = [1,null,3]

# Output: [1,3]

# Example 4:

# Input: root = []

# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # use level order traversal to get the rightmost node at each level
        if not root:
            return []

        rightmost_values = []
        current_level = [root]

        while current_level:
            # Get the rightmost value of the current level
            rightmost_values.append(current_level[-1].val)

            # Prepare for the next level
            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level

        return rightmost_values
    
# Example usage:


# Create a sample binary tree: 1 -> 2, 3 -> null, 5, null, 4
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3, None, TreeNode(4))
root.left.right = TreeNode(5)

solution = Solution()
print(solution.rightSideView(root))  # Output: [1, 3, 4]

# Test with an empty tree
empty_tree = None
print(solution.rightSideView(empty_tree))  # Output: []