# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = k
        return self.inOrder(root) or 0
    
    def inOrder(self, node):
        if node == None:
            return None
        val = self.inOrder(node.left)
        if val:
            return val
        
        self.count -= 1
        if self.count == 0:
            return node.val
        
        val = self.inOrder(node.right)
        if val:
            return val
