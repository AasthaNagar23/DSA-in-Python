class tn:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def Balanced(root):

    def height(node):
        if node is None:
            return 0

        left = height(node.left) #recursion pehle hi laga chuke he 
        if left == -1:
            return -1

        right = height(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1
            
        return max(left, right) + 1    #for every node

    return height(root) != -1


# Creating the tree
root = tn(1)
root.left = tn(2)
root.right = tn(3)
root.left.left = tn(4)
root.left.right = tn(5)

print(Balanced(root))