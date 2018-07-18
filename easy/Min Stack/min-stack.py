"""
Problem:

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.array.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        del self.array[-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.array[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.array)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
