# https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.hasOne(root)
        return root
        
    def hasOne(self, root):
        if(root == None):
            return True
        if not self.hasOne(root.left):
            root.left = None
        if not self.hasOne(root.right):
            root.right = None
        if((self.hasOne(root.left) or self.hasOne(root.right)) and (root.left != None) or root.right != None):
            return True
        return root.val == 1
