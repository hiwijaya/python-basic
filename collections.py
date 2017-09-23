# LIST
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




