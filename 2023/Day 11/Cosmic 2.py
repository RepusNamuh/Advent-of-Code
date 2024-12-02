import copy
with open("Day 11\Cosmic.txt", 'r') as f:
    data = f.read().splitlines()

data = [list(line) for line in data]

change = 9999 # Degree of space expansion
x_len = len(data[0])
y_len = len(data)

# recording original hash postion
pos = []
for r in range(y_len):
    for c in range(x_len):
        if data[r][c] == "#":
            pos.append((float(r), float(c)))

# Changing x coordinate of each hash according to 'change'
delta_depth = 0
for i in range(y_len):
    if all(data[i][r] == '.' for r in range(x_len)):
        for  j, tup in enumerate(pos):
            if tup[0] > i + delta_depth:
                pos[j] = (tup[0] + change, tup[1])
        delta_depth += change

# Changing y coordinate of each hash according to 'change'
delta_len = 0
for c in range(x_len):
    if all(data[r][c] == '.' for r in range(y_len)):
        for  j, tup in enumerate(pos):
            if tup[1] > c + delta_len:
                pos[j] = (tup[0], tup[1] + change)
        delta_len += change

# Calculating total by subtraction of coordinate
total = 0
for i in range(len(pos)):
    for j in range(i + 1, len(pos)):
        row_dis = abs(pos[j][0] - pos[i][0])
        col_dis = abs(pos[j][1] - pos[i][1])
        total += row_dis + col_dis 

print(total)