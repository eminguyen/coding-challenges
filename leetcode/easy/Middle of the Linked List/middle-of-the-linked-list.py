"""
Problem:

Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        length = 1
        while(node.next != None):
            length += 1
            node = node.next
        node = head
        for i in range(length // 2):
            node = node.next
        return node
