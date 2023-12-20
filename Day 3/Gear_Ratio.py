from collections import defaultdict

file = open("Day 3\Gear_Ratio.txt", 'r')
line_dict = {}
gear_adjecent = defaultdict(list)
total = 0
answer = 0
ok = False
gear = False
temp_total = ""
gears = []
for line_num, row in enumerate(file):
    line_dict[line_num] = row.split("\n")[0]
    max_line = line_num

for line_num, row in line_dict.items():
    for pos, c in enumerate(row):
        if c.isdigit():
            temp_total += c
            for q in [ -1,0, 1]:
                for s in [-1, 0, 1]:
                    if 0<=line_num + q < max_line and 0<= pos + s < len(row):
                        row = line_dict[line_num + q]
                        ch = row[pos + s]
                        if ch != "." and not ch.isdigit():
                                ok = True  
                        if ch == '*':
                            gears.append((line_num + q, pos + s))
                            gear = True

        else:
            if gear: 
                gear_adjecent[gears.pop()].append(int(temp_total)) 
                gear = False
            if ok:
                total += int(temp_total)  
                ok = False
            temp_total = ""

for pos, gear in gear_adjecent.items():
    #print(gear, True if len(gear) == 2 else False)
    answer += gear[0] * gear[-1] if len(gear) == 2 else 0
    
print(total)   
print(answer)
