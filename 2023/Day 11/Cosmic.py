import copy
with open("my_result.txt", 'r') as f:
    data = f.read().splitlines()

data = [list(line) for line in data]

delta_depth = 0
temp_data = data.copy()
for i in range(len(temp_data)):
    if "#" in temp_data[i]:
        continue
    else:
        data.insert(i+1+delta_depth, temp_data[i])
        delta_depth +=1
temp_data = copy.deepcopy(data)
delta_len = 0
for c in range(len(data[0])):
    for r in range(len(data)): 
        if data[r][c] == ".": 
            if r == len(data) - 1:
                for k in range(len(data)):
                    temp = temp_data[k].copy()
                    temp.insert(c + 1 + delta_len, ".")
                    temp_data[k] = temp
                delta_len += 1
            continue
        break
    
hash_table = []
data = temp_data
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == "#":
            hash_table.append((r, c))

total = 0
for i in range(len(hash_table)):
    for j in range(i + 1, len(hash_table)):
        row_dis = abs(hash_table[j][0] - hash_table[i][0])
        col_dis = abs(hash_table[j][1] - hash_table[i][1])
        total += row_dis + col_dis 

print(hash_table)
print(total)