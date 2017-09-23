# # function
# def hallo():
#     print('Hallo there..')
# hallo()
#
#
# # function with parameter
# def hallo_you(name):
#     print('Hallo ' + name)
# hallo_you('Happy')
#
#
# # function with single return value
# def allow_dating_girl(my_age):
#     girl_age = my_age/2 + 7
#     return girl_age
# allowed_girl_age = allow_dating_girl(25)
# print(allowed_girl_age)
#
#
# # function with many return value
# def best_age(my_age):
#     mid_age = my_age // 2
#     next_age = my_age + 1
#     return mid_age, next_age
# (mid_age, next_age) = best_age(25)
# print(mid_age, next_age)


# function with default parameter
def get_sex(sex='unknown'):
    if sex is 'm':
        print('Male')
    elif sex is 'f':
        print('Female')
    else:
        print(sex)
get_sex('m')
