

def my_gen(n):

    print('FIRST')
    yield n

    print('SECOND')
    yield n + 1

    print('THIRD')
    yield n + 2


g = my_gen(5)
print(next(g))
print(next(g))
print(next(g))
