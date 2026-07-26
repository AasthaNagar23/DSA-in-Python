class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create():
    first = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(40)

    first.next = second
    second.next = third
    third.next = fourth

    return first


def reverse(head):   # here we have used three variables prev, current and new_node
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


head = create()

print("Original List:")
display(head)

head = reverse(head)

print("Reversed List:")
display(head)