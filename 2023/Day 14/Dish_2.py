with open("Day 14/Dish.txt", "r") as file:
    data = tuple(file.read().splitlines())

def cycle():
    global data
    for _ in range(4):
        data = tuple(map("".join, zip(*data)))
        data = tuple("#".join(["".join(sorted(list(group), reverse= True)) for group in line.split("#")]) for line in data)
        data = tuple(row[::-1] for row in data)

seen = {data}
array = [data]
iter = 0
while True:
    iter += 1
    cycle()
    if data in seen:
        break
    seen.add(data)
    array.append(data)
    
first = array.index(data)
data = array[(1000000000 - first) % (iter - first) + first]

print(sum([line.count("O") * (len(data) - i) for i, line in enumerate(data)]))