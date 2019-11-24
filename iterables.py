

# Iterables
class Counter:

    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __iter__(self):
        print('__iter__ called')
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.high:
            return self.current

        raise StopIteration


counter = Counter(1, 10)
print(next(counter))
print(next(counter))

for c in counter:
    print(c)


# Iterables to Generator
def generator(low, high):
    current = low - 1
    while current < high:
        current += 1
        yield current


for g in generator(1, 5):
    print(g)
