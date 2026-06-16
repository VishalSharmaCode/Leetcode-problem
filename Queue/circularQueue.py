class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.front = -1
        self.rear = -1
    def isFull(self):
        return (self.rear + 1)%self.capacity ==self.front
    def isEmpty(self):
        return self.front == -1
    def enqueue(self, item):
        if self.isFull():
            return 'Queue Overflow'
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear+1)%self.capacity
        self.queue[self.rear] = item
        return True
    
    def dequeue(self):
        if self.front == -1:
            print('Underflow')
            return
        data = self.queue(self.front)
        if self.front == self.rear:
            self.front =-1
            self.rear =- 1
        else:
            self.front = (self.front +1)%self.capacity
        return data
    