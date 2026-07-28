class tn:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def Diameter(root):
    diameter = 0

    def height(node):   #we need this because at every node diameter will be left height +right height 
    
        nonlocal diameter #this is used as the diameter is in the outer function and if use in the heights modify karna he then we use the nonlocal

        if node is None:
            return 0

        left = height(node.left)
        right = height(node.right)

        diameter = max(diameter, left + right)

        return max(left, right) + 1   #returning the height

    height(root)
    return diameter


# Creating the tree
root = tn(1)
root.left = tn(2)
root.right = tn(3)
root.left.left = tn(4)
root.left.right = tn(5)

print(Diameter(root))