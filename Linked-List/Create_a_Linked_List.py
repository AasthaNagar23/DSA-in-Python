class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def create():
    first=Node(10)
    second=Node(20)
    third=Node(30)
    first.next=second
    second.next=third
    return first
head=create()
