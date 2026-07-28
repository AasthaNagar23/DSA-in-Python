from collections import deque

class tn:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def LevelOrder(root):
    if root is None:
        return

    q = deque([root])      # Queue

    while q:                       #jab tak q empty nahi ho jata                  
        node = q.popleft()     # Remove front node  means take the front node
        print(node.value, end=" ")  #processing the front node 

        if node.left:             #processing its childrens 
            q.append(node.left)

        if node.right:
            q.append(node.right)

# Creating the tree
root = tn(1)
root.left = tn(2)
root.right = tn(3)
root.left.left = tn(4)
root.left.right = tn(5)

LevelOrder(root)