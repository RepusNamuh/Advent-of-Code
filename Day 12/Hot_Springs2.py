with open("my_result.txt", 'r') as f:
    data = f.read().splitlines()

total = 0

for line in data:
    cons, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    spring = []
    temp = []
    add = False
    result = 1
    for i, char in enumerate(cons):
        if char != ".":
            temp.append(char)
            add = True
        if add and char == '.' or i == len(cons)-1:
            spring.append(temp)
            temp = []
            add = False

    if len(cons) == (len(nums) + sum(nums) - 1):
        total += result
        continue 

print(total)