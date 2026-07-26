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

def del_last(head):
    if head is None:
        return None
    if head.next is None:
        return None
    current=head
    while current.next.next:
        current=current.next
    current.next = None
    return head
    
def display(head):
    current=head
    while current:
        print(current.data,end="->")
        current=current.next
    print(None)
    
head=create()
display(head)
head=del_last(head)
display(head)