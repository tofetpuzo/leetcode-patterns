# 530. Minimum Absolute Difference in BST
# Easy
# Topics
# conpanies icon
# Companies
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import List, Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return float('inf')
        # Inorder traversal to get the sorted values of the BST
        def inorder(node: Optional[TreeNode], values: List[int]):
            if node:
                inorder(node.left, values)
                values.append(node.val)
                inorder(node.right, values)
        values = []
        inorder(root, values)
        print(values)  # Debug: print the sorted values from inorder traversal
        # Calculate the minimum absolute difference
        min_diff = float('inf')
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])
        return min_diff
        
        
# Example usage:
if __name__ == "__main__":
    # Create a sample BST: 4 -> 2, 6 -> 1, 3
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(6)
    
    solution = Solution()
    print(solution.getMinimumDifference(root))  # Output: 1
    
    # Test with another BST: 1 -> 0, 48 -> null, null, 12, 49
    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(48, TreeNode(12), TreeNode(49))
    print(solution.getMinimumDifference(root2))  # Output: 1
        


        
        
        
        