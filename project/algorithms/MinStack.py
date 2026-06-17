class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min > value:
            self.min = value

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.min:
            self.min = float("inf")
            for st in self.stack:
                if self.min > st:
                    self.min = st

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min