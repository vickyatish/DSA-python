import sys
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def printLL(self):
        while self.head is not None:
            print(self.head.data, end=' ')
            self.head = self.head.next

def addTwoLinkedList(l1, l2):
    dummy = Node(-1)
    temp = dummy
    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum+=l1.data
            l1 = l1.next
        if l2:
            sum+=l2.data
            l2 = l2.next
        if carry:
            sum+=carry
        carry = sum//10
        temp.next = Node(sum%10)
        temp = temp.next
    return dummy.next

def print_head(head):
    while head:
        print(head.data, end='->')
        head = head.next

if __name__ == '__main__':
    l1 = Node(0)
    l1.next = Node(1)
    l1.next.next = Node(3)

    l2 = Node(1)
    l2.next = Node(3)

    new_head = addTwoLinkedList(l1, l2)
    print_head(new_head)
    sys.exit("")


