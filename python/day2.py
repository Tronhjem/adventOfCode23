
with open("../data/2.txt") as file:
    data = file.readlines()


sdata = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
        ]

# only 12 red cubes, 13 green cubes, and 14 blue cubes?
rules = { 
    'red': 12, 
    'green': 13, 
    'blue': 14
    }

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

# In game 1, three sets of cubes are revealed from the bag 
# (and then put back again). 
# 
# The first set is 3 blue cubes and 4 red cubes; 
# the second set is 1 red cube, 2 green cubes, and 6 blue cubes; 
# the third set is only 2 green cubes.


# ====================================================
## FIRST
# possibleGames = 0
# for line in data:

#     line = line.replace('\n', '')
#     gameId = line.split(':')[0].split(' ')[1]
#     rounds = line.split(':')[1].split(';')

#     gamePossible = True  
#     for round in rounds:
#         cubes = round.split(',')
#         for cube in cubes:
#             split = cube.split(' ')
#             number = split[1]
#             color = split[2]
#             ruleMax = rules[color]
#             if int(number) > ruleMax:
#                 gamePossible = False

#     if gamePossible:
#         possibleGames += int(gameId)
# ====================================================

sum = 0
for line in data:

    line = line.replace('\n', '')
    gameId = line.split(':')[0].split(' ')[1]
    rounds = line.split(':')[1].split(';')

    requirement = { 
        'red': 0, 
        'green': 0, 
        'blue': 0
        }

    for round in rounds:
        cubes = round.split(',')
        for cube in cubes:
            split = cube.split(' ')
            number = split[1]
            color = split[2]
            required = requirement[color]
            if int(number) > required:
                requirement[color] = int(number)


    power = 1
    for entry in requirement:
        power *= requirement[entry] 
    print(power)

    sum += power

print (sum)
====================================================

print(possibleGames)

