"""
Stack Implementation using List
"""

class StackUsingList:
    def __init__(self):
        self.__stack = []  # private stack

    def push(self, data):
        self.__stack.append(data)
        print(f"Pushed {data} into Stack")

    def size(self):
        return len(self.__stack)

    def is_empty(self):
        return len(self.__stack) == 0

    def top(self):
        if self.is_empty():
            print("Stack is Empty, No top element")
            return None
        return self.__stack[-1]

    def pop(self):
        if self.is_empty():
            print("Stack is Empty, Cannot pop")
            return None
        popped = self.__stack.pop()
        print(f"Popped {popped} from Stack")
        return popped

    def display(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print("Stack (top -> bottom):", list(reversed(self.__stack)))


myStack = StackUsingList()
print(myStack.is_empty())  # True

myStack.push(9)
myStack.push(8)
myStack.push(7)
myStack.push(6)

l = [5, 4, 3, 2, 1, 0]
for i in l:
    myStack.push(i)

myStack.display()  # Should show stack from top (0) to bottom (9)

print("Is Empty:", myStack.is_empty())
print("Top Element:", myStack.top())

print("Popped Element:", myStack.pop())
myStack.display()
