import re

with open("2024/Day 3/Mull It Over.txt") as f:
    data = f.read().splitlines()

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

relevant_data = []
for line in data:
    matches = re.findall(pattern, line)
    relevant_data.extend(matches)

def part1(data):
    data = [list(map(int, (re.sub(r'\D+', ' ', text).strip()).split())) for text in data]
    return sum([block[0] * block[1] for block in data if len(block) != 0])

def part2(data):
    temp = data[:]
    multiply = True
    total = 0
    for i in range(len(temp)):
        if "don't()" in temp[i]:
            multiply = False
        elif "do()" in temp[i]:
            multiply = True
        else:
            if multiply:
                block = list(map(int, (re.sub(r'\D+', ' ', temp[i]).strip()).split()))
                total += block[0] * block[1]

    return total
print(part1(relevant_data))
print(part2(relevant_data))