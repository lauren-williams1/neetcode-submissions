class MinStack:
    def __init__(self):
        # create stack 1
        self.stack = []

        #create a minimum stack
        self.minStack = []

    def push(self, val: int) -> None:
        # append the value to the stack
        # we also use min function to decide, if we use current value or top of min stack for min value
        # save it as a val

        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    def pop(self) -> None:
        # pop from stack
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # we just see teh value nothing get's deleted or added
        return self.stack[-1]

    def getMin(self) -> int:
        # we just see the value thing get's deleted or added
        return self.minStack[-1]