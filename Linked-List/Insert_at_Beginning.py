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

def insert_beginning(head,data):
    newNode=Node(data)
    newNode.next=head
    head=newNode
    return head
    
def display(head):
    current=head
    while current:
        print(current.data,end="->")
        current=current.next
    print(None)
    
head=create()
display(head)
head=insert_beginning(head,90)
display(head)