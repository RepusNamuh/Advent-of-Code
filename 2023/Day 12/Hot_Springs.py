with open("Day 12/Hot_Springs.txt", 'r') as f:
    data = f.read().splitlines()

total = 0

cache = {}
def count(cons, nums):
    if cons == "":
        return 1 if nums ==() else 0  
    if nums == ():
        return 0 if "#" in cons else 1
    
    result = 0
    
    key = (cons, nums)
    if key in cache:
        return cache[key]
    
    if cons[0] in ".?":
        result += count(cons[1:], nums)
    if cons[0] in "#?":
        if nums[0] <= len(cons) and "." not in cons[:nums[0]] and (nums[0] == len(cons) or cons[nums[0]] != "#"):
            result += count(cons[nums[0]+1:], nums[1:])
    
    cache[key] = result
    return result

for line in data:
    cons, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    cons = "?".join([cons]*5)
    nums *= 5
    total += count(cons, nums)

print(total)