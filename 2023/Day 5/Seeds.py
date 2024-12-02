from collections import defaultdict
# input data
with open('Day 5\Seeds.txt', 'r') as f:
    data = f.read()

# Seperating seeds and data that transpose one material to another
seeds, *maps = data.split("\n\n")

# Assigning element of seeds into a list as integer
list1 = list(map(int, seeds.split(":")[1].split()))
# Assigning every two elements in a tuple
lists = [(list1[i], list1[i] + list1[i + 1]) for i in range(0, len(list1), 2)]

# Looping through each transition until location
for lines in maps:
    temp_list1 = list1.copy() # Temporarily copy list
    temp_list2 = []
    
    # Part one of Day 5
    for x, s in enumerate(list1):
        # Looping through every formula in each transition
        for line in lines.splitlines()[1:]:
            proc, src, sz = (int(x) for x in line.split())
            if s in range(src, src + sz):
                temp_list1[x] = s - src + proc

    # Looping through each tuple of seed
    while lists:
        begin, end = lists.pop()
        # Looping through formula for each tuple of seed
        for line in lines.splitlines()[1:]:
            proc, src, sz = (int(x) for x in line.split())
            os = max(begin, src) 
            oe = min(end, src+sz)
            if os < oe:
                temp_list2.append((os - src + proc, oe - src + proc))
                if os > begin:
                    lists.append((begin, os))
                if end > oe:
                    lists.append((oe, end))
                # When break, the current tuple of element will not be change anymore
                break
        # When if condition in for not activated, else condition will be activated.
        else:
            temp_list2.append((begin, end))
        
    lists = temp_list2

    list1 = temp_list1

print(sorted(list1)[0])
print(min(lists)[0])
    



     
