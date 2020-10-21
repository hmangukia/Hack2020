class MyLinkedList(object):
    def __init__(self):
        self.head = None
        # self.size = 0
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid,             return -1.
        """
        if index == 0:
            return self.head.val
        i = 0
        temp = self.head
        while temp != None :
            if i == index:
                # print(temp.val)
                return temp.val
            temp = temp.next
            i += 1
        return -1;
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the   `           insertion, the new node will be the first node of the linked list.
        """
        newNode = ListNode(val)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode
        # print(self.head)    
            
            
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = ListNode(val)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
        # print(self.head)
        
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals         to the length of linked list, the node will be appended to the end of linked list.           If index is greater than the length, the node will not be inserted.
        """
        """
        index = 3
        1 -> 2 -> 3 -> 4
        i = 1
        1  True temp = 2  i=2
        2  True  temp = 3 i=3
        """
        if index == 0:
            self.addAtHead(val)
            
        else:
            newNode = ListNode(val)
            current = self.head
            temp = None
            i = 0
            while i != index and current.next != None:
                temp = current
                current = current.next
                i += 1
            # print(i)
            if i == index:    
                temp.next = newNode
                newNode.next = current
            else:
                self.addAtTail(val)
            # print(self.head)
        
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            newNode = self.head.next
            self.head = newNode
        else:
            i = 0
            current = self.head
            temp = None
            while i != index and current.next != None:
                temp = current
                current = current.next
                i += 1
            if i == index:    
                temp.next = current.next
        # print(self.head)
       
        # print(self.head)
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(1)
# obj.addAtHead(2)
# obj.addAtHead(3)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
