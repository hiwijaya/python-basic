# A INTERVIEW TEST FROM M+

n = input('chocolate N: ')
n = int(n)
values = []
for i in range(n):
    val = input('chocolate value ' + str(i) + ':')
    val = int(val)
    values.append(val)

total = 0
for group_length in range(1, n+1):
    for j in range(n):
        if (j + group_length) > n:
            break
        group = []
        for k in range(group_length):
            idx = j+k
            if idx >= n:
                break
            group.append(values[idx])
        print(group, end='')

        # find minimum in group || otherwise, you can use build in function --> min(group)
        minimum = 0
        for i, val in enumerate(group):
            if i == 0:
                minimum = val
                continue
            if val < minimum:
                minimum = val
        total += minimum
    print('')
print(total)


