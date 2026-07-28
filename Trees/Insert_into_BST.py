class tn:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def Insert(root, val):

    if root is None:
        return tn(val)

    if val < root.value:
        root.left = Insert(root.left, val)
    else:
        root.right = Insert(root.right, val)

    return root
root = tn(4)

def Inorder(root):   #for verifying purpose we can use this 
    if root is None:
        return

    Inorder(root.left)
    print(root.value, end=" ")
    Inorder(root.right)

Inorder(root)


root.left = tn(2)
root.right = tn(7)

root.left.left = tn(1)
root.left.right = tn(3)

root = Insert(root, 5)
Inorder(root)
