class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.key)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    postorder(root)

if __name__ == "__main__":
    main()
