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

def intersection(head1,head2):
    p1=head1
    p2=head2
    while p1!=p2:
        if p1:
            p1=p1.next
        else:
            p1=head2
        if p2:
            p2=p2.next
        else:
            p2=head1
    return p1
    
