from collections import defaultdict
data = open("Day 4\ScratchCard.txt", 'r')

total_point = 0
card_2 = {}
winned_card = defaultdict(int)
global_count = 0

for index, line in enumerate(data):
    num = line.split("\n")[0].split(":")[1]
    game = line.split(":")[0].split()[1]
    winned_card[str(game)] = 0
    card_2[index + 1] = num

for key, value in card_2.items():
    win_count = -1
    win, num = value.split("|")
    win = win.split()
    num = num.split()

    for possible_win in num:
        if possible_win in win:
            #Part 1
            win_count += 1
            point = 2**win_count

    winned_card[str(key)] += 1
    if win_count > -1:
        total_point += point
        
        for (i) in range (key + 1, ((win_count + 2) + key )):
            winned_card[str(i)] += winned_card[str(key)] 

for win in winned_card.values():
    global_count += win 
print(total_point)
print(global_count)
