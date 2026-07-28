class tn:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def Inorder(root):
    if root is None:
        return
    Inorder(root.left)
    print(root.value,end=" ")  # end=" " is very important  
                               #also root.value ka bhi dhyan rakhna
    Inorder(root.right)
    
# Creating the tree
root = tn(1)
root.left = tn(2)
root.right = tn(3)
root.left.left = tn(4)
root.left.right = tn(5)

Inorder(root)