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
for r, row in enumerate(file):
    line_dict[r] = row.split("\n")[0]
    max_line = r

for r, row in line_dict.items():
    for c, ch in enumerate(row):
        if ch.isdigit():
            temp_total += ch
            for rr in [ -1,0, 1]:
                for cc in [-1, 0, 1]:
                    if 0<=r + rr < max_line and 0<= c + cc < len(row):
                        row = line_dict[r + rr]
                        ch = row[c + cc]
                        if ch != "." and not ch.isdigit():
                                ok = True  
                        if ch == '*':
                            gears.append((r + rr, c + cc))
                            gear = True

        else:
            if gear: 
                gear_adjecent[gears.pop()].append(int(temp_total)) 
                gear = False
            if ok:
                total += int(temp_total)  
                ok = False
            temp_total = ""

for c, gear in gear_adjecent.items():
    #print(gear, True if len(gear) == 2 else False)
    answer += gear[0] * gear[-1] if len(gear) == 2 else 0
    
print(total)   
print(answer)
