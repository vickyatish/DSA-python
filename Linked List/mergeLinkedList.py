import sys
class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

def merge(head1, head2):
    current = Node(0)
    head3  = current

    while head1 and head2:
        if head1.data <= head2.data:
            head3.next = head1
            head1 = head1.next
        elif head1.data > head2.data:
            head3.next = head2
            head2 = head2.next
        head3 = head3.next

    if head1:
        head3.next = head1
    elif head2:
        head3.next = head2

    return current.next
    
def print_head(head):
    while head:
        print(head.data, end='->')
        head = head.next

if __name__ == "__main__":
    l1 = Node(1, Node(6, Node(9)))
    l2 = Node(6, Node(7, Node(8)))
    print_head(merge(l1, l2))

    sys.exit("")

    
