class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k
        self.queue = [None for i in range(self.size)]
        # print(self.queue)
        self.front = -1
        self.rear = -1
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if not self.isFull():
            if self.front == -1:    
                self.rear = 0
                self.front = 0
                self.queue[self.rear] = value
            else:
                self.rear = (self.rear + 1) % self.size  
                self.queue[self.rear] = value
            # print(self.queue,self.front,self.rear)
            return True
        else:
            return False
        
        
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if not self.isEmpty():
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            # print(self.queue,self.front,self.rear)
            return True
        else:
            return False
        
    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        
    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
        
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.front == -1:
            return True
        
        return False
    

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if (self.rear == self.size -1 and self.front == 0) or self.rear == self.front - 1:
            return True
        
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
