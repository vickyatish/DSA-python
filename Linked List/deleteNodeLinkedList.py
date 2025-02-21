import sys
class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

def print_head(head):
    while head:
        print(head.data, end='->')
        head = head.next

def deleteNode(node):
    if node.next == None:
        node = None
        return None
    
    node.data = node.next.data
    node.next = node.next.next

    return node


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    print_head(deleteNode(head.next.next.next))