"""
Problem:

Find the sum of all left leaves in a given binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if root == None:
            return 0
        elif root.left != None:
            if root.left.left == None and root.left.right == None:
                sum += root.left.val
        sum += (self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right))
        return sum
