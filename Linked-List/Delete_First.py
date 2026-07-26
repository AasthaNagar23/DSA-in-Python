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

def del_first(head):
    if head is None:
        return None
    
    head=head.next
    return head
    
def display(head):
    current=head
    while current:
        print(current.data,end="->")
        current=current.next
    print(None)
    
head=create()
display(head)
head=del_first(head)
display(head)