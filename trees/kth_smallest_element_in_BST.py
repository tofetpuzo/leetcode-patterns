# Given the root of a binary search tree, and an integer k, 
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    def kth_smallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        
        count = [k]
        ans = [0]
        
        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)

            if count[0] == 1:
                ans[0] = node.val
                
            count[0] -= 1
            
            if count[0] > 0:
                inorder(node.right)
            
        inorder(root)
        return ans[0]