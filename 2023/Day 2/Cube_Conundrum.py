file = open("Day 2\Cube_Conundrum.txt", 'r')

id_sum = 0
max_cube = {"red": 12, "green": 13, "blue": 14}
cube_sum = 0

for line in file:
    break_true = False
    game, line = line.split(":")
    game_record = game.split()[1]
    min_cube = {"red": 0, "green": 0, "blue": 0}
    
    for turn in line.split(";"):
        for cube in turn.split(","):
            num, colour = cube.split()
            num = int(num)
            if num > max_cube.get(colour, 0):
                break_true = True
            min_cube[colour] = max(min_cube[colour], num)

    cube_sum += min_cube["red"]*min_cube["green"]*min_cube['blue']
    if not break_true:
        id_sum += int(game_record)
        cube_sum += min_cube["red"]*min_cube["green"]*min_cube['blue']

print(id_sum)
print(cube_sum)

            
                     