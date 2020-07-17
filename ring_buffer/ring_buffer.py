class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.info = []
        self.oldest = 0

    def append(self, item):
        if len(self.info) < self.capacity:
            self.info.append(item)
        else:
            self.info[self.oldest] = item
            self.oldest += 1
        if self.oldest == self.capacity:
            self.oldest = 0

    def get(self):
        return self.info