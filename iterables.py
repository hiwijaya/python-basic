
class Counter:

    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __iter__(self):
        print('iter')
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.high:
            return self.current

        raise StopIteration


counter = Counter(1, 10)
print(next(counter))
print(next(counter))
print('-----')

for c in counter:
    print(c)

for c in counter:
    print(c)
