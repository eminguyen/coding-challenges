"""
Problem:

You’re given the pointer to the head node of a linked list and the position of a node to delete. 
Delete the node at the given position and return the head node. 
A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. 
The list may become empty after you delete the node.
"""


# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    currNode = head
    prevNode = head
    if position == 0:
        return head.next
    for i in range(position):
        prevNode = currNode
        currNode = currNode.next
    prevNode.next = currNode.next
    return head
