class MyStack:
    def __init__(self):
        self.que1 = []
        self.que2 = []

    def push(self, x: int) -> None:
        self.que1.append(x)

    def pop(self) -> int:
        while len(self.que1) != 1:
            self.que2.append(self.que1.pop(0))
        x = self.que1.pop(0)

        self.que1, self.que2 = self.que2, self.que1
        return x

    def top(self) -> int:
        while len(self.que1) != 1:
            self.que2.append(self.que1.pop(0))
        x = self.que1.pop(0)

        self.que2.append(x)
        self.que1, self.que2 = self.que2, self.que1
        return x

    def empty(self) -> bool:
        return len(self.que1) == 0