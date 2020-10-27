class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack  = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        print("push",self.stack)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        print("pop",self.stack)
        return self.stack.pop(0)
        
        
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        
        print("peek",self.stack)
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        
        print("empty",self.stack)
        if len(self.stack) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
