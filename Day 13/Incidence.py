with open("Day 13/Incidence.txt", 'r') as f:
    data = f.read().split("\n\n")

total = 0
def mirror(blocks):
    for i in range(1, len(blocks)):
        real = blocks[:i][::-1]
        image = blocks[i:]

        if sum(sum(0 if a == b else 1 for a,b in zip(x, y)) for x, y in zip(real,image)) == 1:
            return i
        
    return 0

for blocks in data:
    blocks = blocks.splitlines()
    
    total += 100 * mirror(blocks) + mirror(list(zip(*blocks)))
print(total)

