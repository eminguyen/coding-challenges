"""
Problem:

If you're new to linked lists, this is a great exercise for learning about them. 
Given a pointer to the head node of a linked list, print its elements in order, one element per line. 
If the head pointer is null (indicating the list is empty), don’t print anything.
"""

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    while head != None:
        print(head.data)
        head = head.next
