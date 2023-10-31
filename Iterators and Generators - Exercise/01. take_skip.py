class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.count:
            tmp = self.start
            self.start += self.step
            self.counter += 1
            return tmp

        raise StopIteration()


numbers = take_skip(2, 6)

for number in numbers:
    print(number)
