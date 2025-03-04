def findDuplicateN1(arr):
    sorted_arr = sorted(arr)

    for i in range(len(arr)-1):
        if sorted_arr[i]==sorted_arr[i+1]:
            return sorted_arr[i]
    
def findDuplicateN2(arr):
    dict = {}

    for a in arr:
        if a in dict:
            return a
        else:
            dict[a]=1

    return -1

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def findDuplicateN3(head):

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = second

    # Check if there is a loop
    # in the linked list
    if findDuplicateN3(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")
    