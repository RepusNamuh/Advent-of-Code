from collections import Counter

with open("2024\Day 1\Historian_Historia.txt") as f:
    data = [line.strip().split() for line in f]
    list1 = []
    list2 = []
    for line in data:
        list1.append(line[0])
        list2.append(line[1])
   
total = 0
total1 = 0

list1 = sorted(list1)
list2 = sorted(list2)

for i in range(len(list1)):
    total += abs(int(list1[i]) - int(list2[i]))

location_count = Counter(list2)

for location in list1:
    total1 += location_count[location] * int(location)

print(total, total1)
