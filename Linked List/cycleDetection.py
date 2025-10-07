class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def detect_cycle(head):
    """Return True if a cycle exists, False otherwise."""
    pass  # TODO: implement Floyd’s tortoise-hare or any preferred method
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    # Sample setup
    nodes = [ListNode(i) for i in range(5)]
    for i in range(4):
        nodes[i].next = nodes[i + 1]
    nodes[-1].next = nodes[2]  # creates a cycle

    has_cycle = detect_cycle(nodes[0])
    print(f"Cycle detected: {has_cycle}")
