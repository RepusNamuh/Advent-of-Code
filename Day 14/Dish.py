with open("Day 14/Dish.txt", "r") as file:
    data = file.read().splitlines()

total = 0
length = len(data)
data = [list(line) for line in data]

def rolling(row, pos, char, current):
    global data
    global total 
    if row - 1 >= 0 and data[row-1][pos] == ".":
        data[row - 1][pos] = char
        rolling(row -1, pos, char, current)
    if row != current:
        data[row+1][pos] = "."
    total += (length - row) if data[row][pos] == "O" else 0

for i in range(len(data)):
    for k in range(len(data[i])):
        if data[i][k] == "O":
            rolling(i, k, "O", i)

print(total)

