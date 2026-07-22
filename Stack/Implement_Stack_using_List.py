class stack:
    def __init__(self):
        self.stack=[]
    # pushing an element
    def push(self,item):
        self.stack.append(item)
    # deleting an element
    def pop(self):
        if len(self.stack)==0:
            print("stack is empty")
        self.stack.pop()
    # top element
    def peek(self):
        if len(self.stack)==0:
            print("stack is empty")
        return self.stack[-1]
    # checking if the list is empty 
    def is_empty(self):
        return len(self.stack)==0
    # displaying the list
    def display(self):
        print(self.stack)
s=stack()
s.push(10)
s.push(20)
s.pop()
s.display()
s.pop()
s.display()
print(s.is_empty())