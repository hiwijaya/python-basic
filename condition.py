age = 25

if age < 21:
    print('No beer for you!')
else:
    print('Cheers!')


name = 'Yanna'
if name is 'Happy':
    print('Hallo Happy!')
elif name is 'Yanna':
    print('Hi, beauty..')
else:
    print('Who the fuck are you?')


# ternary conditional
drink = 'Beer' if age >= 21 else 'Orange Juice'
print(drink)

# different between 'is' and '=='
# 'is' for REFERENCE EQUALITY. --> beware when using it!
# '==' for VALUE EQUALITY.
a = 5000
b = 5000
print(a is 500 * 10)
print(a == 500 * 10)
print(a is b)



