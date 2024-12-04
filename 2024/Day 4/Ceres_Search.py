with open("2024/Day 4/Ceres_Search.txt") as f:
    data = f.read().splitlines()
    data = [list(line) for line in data]

neighbour_array = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
neighbour_array2 = [[[[-1, -1], [1, 1]], [[-1, 1], [1, -1]]]]

def XMAS_Search(data, x, y, row, col):
    if row + 3 * x < 0 or col + 3 * y < 0:
        return False
    try:
        if data[row + 1 * x][col + 1 * y]== "M":
            if data[row + 2 * x][col + 2 * y]== "A":
                if data[row + 3 * x][col + 3 * y]== "S":
                    return True
    except:
          return False
    return False

def search(data):
    total = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == "X":
                for x, y in neighbour_array:
                    if XMAS_Search(data, x, y, row, col):
                        total += 1
    return total

def orientaion_search(data, row, col, orientation):
    coor1, coor2 = orientation
    x1, y1 = coor1
    x2, y2 = coor2
    if data[row + x1][col + y1] == "M" and data[row + x2][col + y2] == "S":
        return True
    elif data[row + x1][col + y1] == "S" and data[row + x2][col + y2] == "M":
        return True
    return False

def X_MAS_Search(data, row, col, orientation):
    if row - 1 < 0 or col - 1 < 0:
        return False
    cross1 = False
    cross2 = False
    try:
        cross1 = orientaion_search(data, row, col, orientation[0])
        cross2 = orientaion_search(data, row, col, orientation[1])
        return cross1 and cross2
    except:
          return False

def search2(data):
    total = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == "A":
                for orientation in neighbour_array2:
                    if X_MAS_Search(data, row, col, orientation):
                        total += 1
    return total
print(search2(data))
