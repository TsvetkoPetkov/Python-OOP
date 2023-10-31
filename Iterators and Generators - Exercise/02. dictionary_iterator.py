class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())
        self.start_inx = -1
        self.end_inx = len(self.items) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_inx == self.end_inx:
            raise StopIteration

        self.start_inx += 1

        return self.items[self.start_inx]


result = dictionary_iter({1: "1", 2: "2"})

for x in result:
    print(x)
