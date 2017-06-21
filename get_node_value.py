"""
You’re given the pointer to the head node of a linked list and a specific
position. Counting backwards from the tail node of the linked list, get the
value of the node at the given position. A position of 0 corresponds to the tail,
1 corresponds to the node before the tail and so on.

Input Format
You have to complete the int GetNode(Node* head, int positionFromTail) method
which takes two arguments - the head of the linked list and the position of the
node from the tail. positionFromTail will be at least 0 and less than the number
of nodes in the list. You should NOT read any input from stdin/console.

Output Format
Find the node at the given position counting backwards from the tail. Then
return the data contained in this node. Do NOT print anything to stdout/console.

"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def GetNode(head, position):
    # traverse the list and add the data to a stack
    stack = []
    while head:
        stack.append(head.data)
        head = head.next

    # once you get to the end, take the -(position + 1)
    return stack[-(position + 1)]
