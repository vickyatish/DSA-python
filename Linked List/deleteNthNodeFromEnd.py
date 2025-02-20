import sys
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def printLL(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next

def deleteNthNodeFromEnd(head, N):
    
    if N==1:
        temp = head
        while head.next.next:
            head = head.next
        head.next = None
        return temp
    
    temp = head
    n = 0
    while temp:
        n+=1
        temp = temp.next
    
    if n==N:
        head = head.next
        return head
    
    res = n-N-1
    temp = head
    while res:
       temp = temp.next
       res-=1

    print("you are now at ", temp.data)

    deleteNode = temp.next
    temp.next = temp.next.next
    deleteNode = None

    return head

arr = [1, 2, 3, 4, 5]
N = 5
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
head.next.next.next.next = Node(arr[4])

# Delete the Nth node from the end and print the modified linked list
head = deleteNthNodeFromEnd(head, N)
printLL(head)

sys.exit("")

    
