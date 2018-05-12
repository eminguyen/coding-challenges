"""
Problem:

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list = [0]
        node1 = l1
        node2 = l2
        while(node1 is not None or node2 is not None):
            if(node1 is not None):
                list[-1] += node1.val
                node1 = node1.next
            if(node2 is not None):
                list[-1] += node2.val
                node2 = node2.next
            carry = list[-1] // 10
            list[-1] %= 10
            if(node1 is not None or node2 is not None or carry > 0 ):
                list.append(carry)
        return list
