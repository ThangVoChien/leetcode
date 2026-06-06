class MyQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        while len(self.st1) != 1:
            self.st2.append(self.st1.pop())
        x = self.st1.pop()

        while len(self.st2) != 0:
            self.st1.append(self.st2.pop())
        return x

    def peek(self) -> int:
        while len(self.st1) != 1:
            self.st2.append(self.st1.pop())
        x = self.st1.pop()

        self.st1.append(x)
        while len(self.st2) != 0:
            self.st1.append(self.st2.pop())
        return x

    def empty(self) -> bool:
        return len(self.st1) == 0