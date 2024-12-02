from collections import defaultdict
from math import gcd

with open("Day 8\Haunted_Wasteland.txt", 'r') as f:
    data = f.read()

direction_list = data.split("\n\n")[0] # Getting the LRLR... part

# Turning the left right direction into index for easy access
direction_list = direction_list.replace("R", "1")
direction_list = direction_list.replace("L", "0")

direction_binary = list(map(int, direction_list)) # Turning this into list of int

# Creating a dictionary of path, that is 
location_list = defaultdict(list)
for location in data.split("\n\n")[1].split("\n"):
    nodes,  element= location.split(" = ")
    element = element.replace("(", "")
    element = element.replace(")", "")
    element_set = []
    for direction in element.split(", "):
        element_set.append(direction)
    location_list[nodes] = element_set

destination = "AAA"
step = 0
while destination != "ZZZ":
    for i in direction_binary:
        destination = location_list[destination][i]
        step += 1
        if destination == "ZZZ":
            break

### Part 2
location_list_1 = location_list.copy()
destination1 = [key for key in location_list_1 if key.endswith("A")]

steps = 1 # For final calculation
# Step until the first node with last letter == "Z"
step_count = [0 for i in range(len(destination1))] 

# Loop through each of the starting element until the first Z of each element
for index, location in enumerate(destination1):
    while not location.endswith("Z"):
        for i in direction_binary:
            location = location_list_1[location][i]
            step_count[index] += 1
            if location.endswith("Z"):
                destination1[index] = location
                break

lcm = step_count.pop()
for num in step_count:
    lcm = lcm * num // gcd(lcm, num)


print(step, lcm)