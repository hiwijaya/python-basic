
def my_generator(n):

    print('FIRST')
    yield n

    print('SECOND')
    yield n + 1

    print('THIRD')
    yield n + 2


g = my_generator(1)
print(next(g))
print(next(g))
print(next(g))
