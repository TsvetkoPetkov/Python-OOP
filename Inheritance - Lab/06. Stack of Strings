from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        el = self.data.pop()

        return el

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        else:
            return True

    def __str__(self):
        return f"[{', '.join([str(el) for el in reversed(self.data)])}]"
