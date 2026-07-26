class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create Linked List
def create(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head


# Display Linked List
def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Remove Nth Node From End
def removeNthFromEnd(head, n):
    # Create dummy node
    dummy = Node(0)
    dummy.next = head
    slow = dummy
    fast = dummy
    # Move fast n+1 steps
    for i in range(n + 1):
        fast = fast.next
    # Move both pointers
    while fast:
        slow = slow.next
        fast = fast.next
    # Delete the nth node from end
    slow.next = slow.next.next
    return dummy.next


head = create([10, 20, 30, 40, 50])
print("Original Linked List:")
display(head)
n = 2
head = removeNthFromEnd(head, n)
print("After Removing {n}nd Node From End:")
display(head)