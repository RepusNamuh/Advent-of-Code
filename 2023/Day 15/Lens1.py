from collections import defaultdict
with open("Day 15/Lens.txt", "r") as file:
    data = file.read().split(",")

total = 0
for string in data:
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256
    total += current
print(total)