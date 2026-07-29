class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def create(arr):
    if len(arr)==0:
        return None
    head=Node(arr[0])
    temp=head
    for i in range(1,len(arr)):
        new=Node(arr[i])
        temp.next=new
        temp=temp.next
    return head

def merge(head1,head2):
    dummy = Node(0)
    tail=dummy
    while head1 and head2:
        if head1.data <= head2.data:
            tail.next=head1
            head1=head1.next
        else:
            tail.next=head2
            head2=head2.next
        tail=tail.next
    if head1:
        tail.next=head1
    else:
        tail.next=head2
    return dummy.next
    
def display(head):
    temp=head
    while temp:
        print(temp.data,end=" -> ")
        temp=temp.next
    print("None")

arr1=[1,5,8,10]
arr2=[3,4,9,12]
a=create(arr1)
b=create(arr2)
display(a)
display(b)
c=merge(a,b)

display(c)
