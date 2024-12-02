import math

with open("Day 6\Wait_For_It.txt", 'r') as f:
    data = f.read()

time, distance = data.splitlines()
time = list(map(int, time.split(":")[1].split()))
distance = list(map(int, distance.split(":")[1].split()))

time1 = ""
for i in time:
    time1 += str(i)

distance1 = ""
for i in distance:
    distance1 += str(i)

time1, distance1 = int(time1), int(distance1)

total = 1
total1 = 0

for i in range(0, len(time)):
    for j in range(math.ceil(distance[i] / time[i]), time[i]):
        if (j * (time[i] - j)) > distance[i]:
            break

    total *= ((time[i] - j) - j + 1)

for j in range(math.ceil(distance1 / time1), math.ceil(time1 / 2)):
    if (j * (time1 - j)) > distance1:
            break

total1 = (time1 - j) - j + 1

print(total)
print(total1)