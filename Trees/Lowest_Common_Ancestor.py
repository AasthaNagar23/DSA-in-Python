class tn:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class tn:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def LCA(root, p, q):

    if root is None:
        return None

    if root == p or root == q:
        return root

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if left and right:
        return root

    return left if left else right


root = tn(3)

root.left = tn(5)
root.right = tn(1)

root.left.left = tn(6)
root.left.right = tn(2)

root.right.left = tn(0)
root.right.right = tn(8)

root.left.right.left = tn(7)
root.left.right.right = tn(4)

p = root.left                  # Node 5
q = root.left.right.right      # Node 4

ans = LCA(root, p, q)

print(ans.value)