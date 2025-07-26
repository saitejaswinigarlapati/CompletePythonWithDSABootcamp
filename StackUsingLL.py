"""
Stack Implementation using Linked List

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed: {data}")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow!")
            return None
        popped = self.top.data
        self.top = self.top.next  # Move top to next node
        print(f"Popped: {popped}")
        return popped

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.top.data

    def display(self):
        current = self.top
        if self.is_empty():
            print("Stack is empty.")
            return
        print("Stack elements (top to bottom):")
        while current:
            print(current.data)
            current = current.next

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.display()

print("Top element is:", stack.peek())

stack.pop()
stack.display()
