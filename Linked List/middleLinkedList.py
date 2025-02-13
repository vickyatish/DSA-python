class Node:
    def __init__(self, data,next=None):
        self.data = data
        self.next = next

def findMiddle(head):
    fast = head
    slow = head

    while fast and fast.next and slow:
        fast = fast.next.next
        slow = slow.next


    print(slow.data) 
    

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    findMiddle(head)