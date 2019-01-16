# function
def hallo():
    print('Hallo there..')


hallo()


# function with parameter
def hallo_you(name):
    print('Hallo ' + name)


hallo_you('Happy')


# function with single return value
def allow_dating_girl(my_age):
    girl_age = my_age/2 + 7
    return girl_age


allowed_girl_age = allow_dating_girl(25)
print(allowed_girl_age)


# function with many return value
def best_age(my_age):
    mid_age = my_age // 2
    next_age = my_age + 1
    return mid_age, next_age


(mid_age, next_age) = best_age(25)
print(mid_age, next_age)


# function with keyword parameter/arguments
def dumb_sentence(name='Happy', action='eat', item='burger'):
    print(name, action, item)


dumb_sentence()
dumb_sentence('Nemo', 'split', 'gently')
dumb_sentence(action='cook')
dumb_sentence(item='sandwich', action='cook')


# flexible number of arguments
def add_numbers(*args):
    total = 0
    for i in args:
        total += i
    print('Total: ', total)


add_numbers(1, 2, 3, 4, 5, 6)


# unpacking arguments
def formula(height, width, depth):
    print(height * width * depth)


input_1 = [10, 5, 4]
formula(*input_1)


# LAMBDA function
distance = lambda speed, time: speed * time
print(distance(10, 15))
