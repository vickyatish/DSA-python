"""Template for computing Y-intersection between two singly linked lists."""

from __future__ import annotations
from typing import Optional


class Node:
    """Simple singly linked list node."""

    __slots__ = ("data", "next")

    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional[Node] = None


def find_y_intersection(head_a: Optional[Node], head_b: Optional[Node]) -> Optional[Node]:
    """Return the intersection node shared by both lists, if any."""
    # TODO: Implement the actual intersection detection logic.
    p1, p2 = head_a, head_b
    
    while p1!=p2:
        p1 = p1.next if p1 else head_b
        p2 = p2.next if p2 else head_a

    return p1


def _build_sample_lists() -> tuple[Optional[Node], Optional[Node]]:
    """Create two sample linked lists that intersect at a shared node."""
    # Shared tail
    shared = Node(8)
    shared.next = Node(10)

    # First list: 3 -> 6 -> 9 -> 8 -> 10
    head_a = Node(3)
    head_a.next = Node(6)
    head_a.next.next = Node(9)
    head_a.next.next.next = shared

    # Second list: 4 -> 8 -> 10 (shares the tail from the first list)
    head_b = Node(4)
    head_b.next = shared

    return head_a, head_b


def main() -> None:
    head_a, head_b = _build_sample_lists()
    intersection = find_y_intersection(head_a, head_b)

    if intersection is None:
        print("No intersection detected.")
    else:
        print(f"Intersection at node with value: {intersection.data}")


if __name__ == "__main__":
    main()
