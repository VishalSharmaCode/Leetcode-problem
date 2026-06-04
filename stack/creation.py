class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] *capacity
        self.top = -1
    def push(self, ele):
        if self.isFull():
            print('Stack Overflow')
            return False
        self.top +=1
        self.stack[self.top] = ele
        return True
    
    def pop(self):
        if self.isEmplty():
            print('Stack Underflow')
            return None
        item =self.stack[self.top]
        self.stack[self.top] = None
        self.top -=1
        return item
    
    def peek(self):
        if self.isEmpty():
            print('Stack is empty')
            return
        return self.stack[self.top]
    
    def isFull(self):
        return self.top == self.capacity - 1
    
    def isEmpty(self):
        return self.top == -1
    
    def display(self):
        if self.isEmpty():
            print('Stack:[]')
            return
        print('Stack(Top -> Bottom):', [self.stack[i] for i in range(self.top, -1, -1)])
    
cap = 20

myStack = ArrayStack(cap)
for i in range(cap):
    myStack.push(i)


myStack.display()

        