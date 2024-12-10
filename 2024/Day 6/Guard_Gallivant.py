import copy
with open('2024/Day 6/Guard_Gallivant.txt') as f:
    data = f.readlines()
    data = [list(x.strip()) for x in data]

def original_position(data):
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char == "^":
                return [x, y]
            
start = original_position(data)
points = ["^", ">", "v", "<"]
direction = [[-1, 0],[0, 1],[1, 0],[0, -1]] # Up, Right, Down, Left

def part1(data, start):
    new_data = copy.deepcopy(data)
    x, y = start
    i, j = direction[0]
    next = 0
    while True:
        if not (0<=x+i<len(data) and 0<=y+j<len(data[0])):
            break
        if data[x+i][y+j] == "#":
            next = (next + 1) % 4
            new_data[x][y] = points[next]
            i, j = direction[next]

        new_data[x+i][y+j] = new_data[x][y]
        new_data[x][y] = "X"
        x, y = x+i, y+j

    return sum([x.count("X") for x in new_data]) + 1

print(part1(data, start))

def part2(data, start):
    total = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            x, y = start
            next = 0
            VISITED = set()
            while True:
                if (x, y, next) in VISITED:
                    total += 1
                    break
                i, j = direction[next]
                VISITED.add((x, y, next))
                if not (0<=x+i<len(data) and 0<=y+j<len(data[0])):
                    break
                if data[x+i][y+j] == "#" or (x + i == row and y + j == col):
                    next = (next + 1) % 4
                else:
                    x, y = x+i, y+j
                
    return total
print(part2(data, start))