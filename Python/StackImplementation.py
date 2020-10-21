class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
   
   
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        print(self.queue)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while(self.queue):
            print(self.queue)
            return self.queue.pop()
        return None


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[len(self.queue)-1]
        # self.array.
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.queue) == 0:
            return True
        return False
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
