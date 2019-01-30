# https://leetcode.com/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level_list = []
        queue = [(root,0)]
        while(len(queue) > 0):
            top = queue.pop(0)
            curr_node = top[0]
            curr_height = top[1]
            if curr_node == None:
                continue
            if(curr_height >= len(level_list)):
                level_list.append([curr_node.val])
            else:
                level_list[curr_height].append(curr_node.val)
            queue.append((curr_node.left, curr_height + 1))
            queue.append((curr_node.right, curr_height + 1))
            
        return level_list[-1][0]
