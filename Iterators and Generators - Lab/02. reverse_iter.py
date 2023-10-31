class reverse_iter:
    def __init__(self, collection):
        self.collection = collection
        self.start_inx = len(self.collection) - 1
        self.end_inx = 0
        self.current_inx = self.start_inx

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_inx < self.end_inx:
            raise StopIteration()

        tmp_inx = self.current_inx
        self.current_inx -= 1
        return self.collection[tmp_inx]


reversed_list = reverse_iter([1, 2, 3, 4])

for item in reversed_list:
    print(item)
