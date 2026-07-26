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


def detect_cycles(head):
    slow=head
    fast=head
    while fast and fast.next: 
        slow=slow.next
        fast=fast.next.next
        if fast==slow:  #yaha thoda dhyan dena 
            return True
    return  False
    
def display(head):
    current=head
    while current:
        print(current.data,end="->")
        current=current.next
    print(None)
    
head=create()
display(head)
dc=detect_cycles(head)
print(dc) 