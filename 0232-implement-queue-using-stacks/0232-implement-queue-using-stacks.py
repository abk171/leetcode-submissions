class MyQueue(object):

    def __init__(self):
        self.st = []
        self.helper = []
        self.front = -1

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.empty():
            self.front = x
        while not self.empty():
            self.helper.append(self.st.pop())
        self.st.append(x)
        while len(self.helper) != 0:
            self.st.append(self.helper.pop())
        

    def pop(self):
        """
        :rtype: int
        """
        result = self.st.pop()
        if not self.empty():
            self.front = self.st[-1]
        return result
        

    def peek(self):
        """
        :rtype: int
        """
        return self.front
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.st) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()