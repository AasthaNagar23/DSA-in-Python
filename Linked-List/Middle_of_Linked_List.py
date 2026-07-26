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

def middle(head):
    slow=head
    fast=head
    while fast and fast.next:  #and yaha hamne two pointers liye he slow and fast
        slow=slow.next
        fast=fast.next.next
    return slow
    
def display(head):
    current=head
    while current:
        print(current.data,end="->")
        current=current.next
    print(None)
    
head=create()
display(head)
mid=middle(head)  #yaha difference aaya he 
print(mid.data) 