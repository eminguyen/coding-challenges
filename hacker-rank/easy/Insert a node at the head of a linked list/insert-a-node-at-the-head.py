"""
Problem:

You’re given the pointer to the head node of a linked list and an integer to add to the list.
Create a new node with the given integer, insert this node at the head of the linked list and return the new head node. 
The head pointer given may be null meaning that the initial list is empty.
"""

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    # Write your code here
    headNode = SinglyLinkedListNode(data)
    if llist == None:
        return headNode
    else:
        headNode.next = llist
    return headNode
