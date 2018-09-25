"""
Problem:

You’re given the pointer to the head node of a doubly linked list. 
Reverse the order of the nodes in the list. The head node might be NULL to indicate that the list is empty. 
Change the next and prev pointers of all the nodes so that the direction of the list is reversed. 
Return a reference to the head node of the reversed list.
"""

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    prevNode = None
    currentNode = head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
    return prevNode
