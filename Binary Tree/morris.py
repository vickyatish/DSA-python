class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorderPredecessor(current):
    pred = current.left

    while(pred.right is not None and pred.right is not current):
        pred = pred.right  

    return pred

def morris_inorder(root):
    current = root
    while current is not None:
        if current.left is None:
            print(current.val)
            current = current.right

        else:
            predecessor = inorderPredecessor(current)
            if predecessor.right is None:
                predecessor.right = current
                current = current.left

            else:
                predecessor.right = None
                print(current.val)
                current = current.right


def main():
    # Sample tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Morris Inorder Traversal:")
    morris_inorder(root)

if __name__ == "__main__":
    main()
