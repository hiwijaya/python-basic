word = 'word'
sentence = "This is sentence."
paragraph = '''You can use triple quotes
to make multiple lines.'''


# Use \ to ignore quotes inside quotes
a = 'I don\'t think so'
print(a)

# f --> formatting string
name = 'happy'
hi_happy = f'hi {name}'
print(hi_happy)

# r --> raw string
b = r'D:\hiwijaya\homework\nudePics'
print(b)

firstname = 'Happy '
print(firstname + 'Indra Wijaya')

# print 5 times
print(firstname * 5)

# get element by index from string
name = 'Happy Indra Wijaya'
print(name[4])

# get element by index start from the last
print(name[-1])

# get element by index with range
print(name[2:8])

# get element with range but start from the beginning
print(name[:4])

# get length of element string
print(len(name))

# print string with a number type use comma
print('hiwijaya', 1992, 10)
