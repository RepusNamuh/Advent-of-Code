import copy
with open("Day 11\Cosmic.txt", 'r') as f:
    data = f.read().splitlines()

data = [list(line) for line in data]

hash_table = []
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == "#":
            hash_table.append((float(r), float(c)))

print(hash_table)
delta_depth = 0
temp_data = data.copy()
empty_row = []
for i in range(len(temp_data)):
    if "#" in temp_data[i]:
        continue
    else:
        empty_row.append(i)
        for  j, tup in enumerate(hash_table):
            if tup[0] > i + delta_depth:
                hash_table[j] = (tup[0] + 999999, tup[1])
        delta_depth += 999999

temp_data = copy.deepcopy(data)
delta_len = 0
empty_col = []
for c in range(len(data[0])):
    for r in range(len(data)): 
        if data[r][c] == ".": 
            if r == len(data) - 1:
                empty_col.append(c)
                for  j, tup in enumerate(hash_table):
                    if tup[1] > c + delta_len:
                        hash_table[j] = (tup[0], tup[1] + 999999)
                delta_len += 999999
            continue
        break
    
data = temp_data

total = 0
for i in range(len(hash_table)):
    for j in range(i + 1, len(hash_table)):
        row_dis = abs(hash_table[j][0] - hash_table[i][0])
        col_dis = abs(hash_table[j][1] - hash_table[i][1])
        total += row_dis + col_dis 

print(hash_table)
print(total)