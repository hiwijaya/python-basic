# LIST ----------------------------------
# List is a sequence data structure with index position. Similar with Array in Java
players = [10, 23, 24, 41]

# get list item with index
print(players[2])

# change value of list item
players[2] = 21
print(players[2])

# change value of list item with range
players[:2] = [0, 0]
print(players)

# add some items on list
players += [47, 50]
print(players)

# or you can do with .append()
players.append(51)
print(players)

# get some item with range
best_players = players[:2]
print(best_players)

# remove an items
players[:2] = []
print(players)


# TUPLE ----------------------------------
# Like list but immutable. It mean the tuples cannot be changed.
rooms = (4, 6, 1, 0.5, 7, 'eight', 'burger')
single_room = (3,)  # to write a tuple containing single value, include a comma

# get tuples item with index, similar with the list
print(rooms[5])

# tuple is immutable, but you are able to take values of existing tuple to create new tuples
extra_rooms = (10, 13)
alot_rooms = rooms + extra_rooms
print(alot_rooms)

# remove individual tuple element is not possible, but you can remove an entire tuple
del alot_rooms
# print(alot_rooms)   # got NameError


# DICTIONARY ----------------------------------
# Data structure with key-value system. Similar with Map in Java.
student = {
    'name': 'Happy Indra Wijaya',
    'age': 25,
    'cool': True
}
print(student)

# accessing element of dict --> or student['name']
student_name = student.get('name')
print(student_name)

# change value element of dict
student['name'] = 'Solomon Grundy'
print(student)