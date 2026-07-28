class tn:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_depth(root):
    if root is None:
        return 0
    left=max_depth(root.left)
    right=max_depth(root.right)
    return max(left,right)+1

# Creating the tree
root = tn(1)
root.left = tn(2)
root.right = tn(3)
root.left.left = tn(4)
root.left.right = tn(5)

print(max_depth(root))   #used the print function 