# while
find = True
num = 0
while find:
    print(num)
    if num is 7:    # lucky number!
        find = False
        break
    num += 1

# loop n times with range()
for n in range(10):         # range(end)
    print(n)
for n in range(1, 5):       # range(start, end)
    print(n)
for n in range(1, 20, 5):   # range(start, end, increment)
    print(n)

# loop n times with repeat()
from itertools import repeat
for name in repeat('Happy', 5):  # user repeat(None, 5) to get increment numbers
    print(name)

# for-loop list
foods = ['soto', 'bakso', 'sate', 'pecel']
for food in foods:
    print(food)

# break
magic_number = '3'
for n in range(10):
    if n is magic_number:
        break
    print(n)

# continue
taken_seat = [1, 4, 6, 7, 9]
for n in range(10):
    if n in taken_seat:
        continue
    print(n)
