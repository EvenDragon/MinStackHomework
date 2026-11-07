class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, x) -> None:
        self.stack.append((x,min(x, self.stack[-1][1]) if self.stack else x))
    def pop(self):
        return self.stack.pop()[0]
    def top(self):
        return self.stack[-1][0]
    def get_min(self):
        return self.stack[-1][1]
stack = MinStack()
stack.push(6)
stack.push(5)
stack.push(-1)
print(stack.get_min())
print(stack.top())
stack.pop()
print(stack.get_min())