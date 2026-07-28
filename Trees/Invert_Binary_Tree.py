class tn:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def Invert(root):
    if root is None:
        return None

    # Swap left and right
    root.left, root.right = root.right, root.left

    # Invert subtrees
    Invert(root.left)
    Invert(root.right)

    return root

# Preorder Traversal (to verify)
def Preorder(root):
    if root is None:
        return
    print(root.value, end=" ")
    Preorder(root.left)
    Preorder(root.right)

# Creating the tree
root = tn(1)
root.left = tn(2)
root.right = tn(3)
root.left.left = tn(4)
root.left.right = tn(5)

print("Before Invert:")
Preorder(root)

Invert(root)

print("\nAfter Invert:")
Preorder(root)