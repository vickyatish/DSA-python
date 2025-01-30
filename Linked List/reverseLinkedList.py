class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    return prev

def print_list(head):
    current = head
    while current:
        print(current.val, end="->")
        current = current.next
    print("None")

head = Node(1, Node(2, Node(3, Node(4))))
print_list(head)
print_list(reverseLinkedList(head))
