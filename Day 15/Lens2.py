from collections import defaultdict
with open("Day 15/Lens.txt", "r") as file:
    data = file.read().split(",")

total = 0
box_dict = defaultdict(int)

def get_hash(label, current, string):
    label = label
    focal_lense = (string[i+1])
    if current in box_dict:
        box_dict[current][label] = focal_lense
    else:
        box_dict[current] = {label: focal_lense}

def remove_hash(label, current):
    label = label
    # Don't ask if key in dict like this if box_dict[current]
    # because it will create a new key in the dict
    if current in box_dict: 
        if label in box_dict[current]:
            del box_dict[current][label]


for string in data:
    current = 0
    label = ""
    for i, char in enumerate(string):
        if char == "=":
            get_hash(label, current, string)
            break
        elif char == "-":
            remove_hash(label, current)
            break
        label += char    
        current += ord(char)
        current *= 17
        current %= 256

for key, value in box_dict.items():
    i = 0
    for k, v, in value.items():
        i += 1
        total += (key+1)*i*int(v)
print(total)