file = open('Day 1/Trebuchet.txt', 'r')
total_1 = 0
total_2 = 0
dict_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
            'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
for line in file:
    digit_1 = []
    digit_2 = []
    for i, s in enumerate(line):
        if s.isdigit():
            digit_1.append((s))
            digit_2.append((s))
        for key in dict_num.keys():
          if line[i:].startswith(key):
            digit_2.append(str(dict_num[key]))

    total_1 += int(digit_1[0] + digit_1[-1])
    total_2 += int(digit_2[0] + digit_2[-1])
        
print(total_1)
print(total_2)
