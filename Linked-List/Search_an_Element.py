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
current=head
element=20
find=False
while current:
    if current.data==element:
        find=True
    current=current.next
    
if find==True:
    print("True")
