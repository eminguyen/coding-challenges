"""
Problem:

You’re given the pointer to the head node of a linked list, an integer to add to the list and the position at 
which the integer must be inserted. Create a new node with the given integer, 
insert this node at the desired position and return the head node.

A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. 
The head pointer given may be null meaning that the initial list is empty.
"""

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    currNode = head
    for i in range(position - 1):
        currNode = currNode.next
    newNode = SinglyLinkedListNode(data)
    newNode.next = currNode.next
    currNode.next = newNode
    return head
