class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.front = -1
        self.rear = -1
    
    def isfull(self):
        return self.rear == self.capacity-1
    def isEmpty(self):
        return self.front == -1 or self.front > self.rear
    def enqueue(self, item):
        if self.isfull():
            print("Queue Overflow")
            return
        if self.front == -1:
            self.front = 0
        self.rear +=1
        self.queue[self.rear] = item
        return True
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front +=1
        if self.front > self.rear:
            self.front= self.rear =-1
        return item
    
    def display(self):
        if self.isEmpty():
            print('Queue: []')
            return
        print('Queue[front -> rear]:', [self.front, self.rear+1])


que = LinearQueue(4)
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)

que.display()
print(que.dequeue())
            