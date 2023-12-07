
with open("../data/test.txt") as file:
    data = file.readlines()


for i in range(len(data)):
    data[i] = data[i].replace('\n','')

DOT = '.'
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# data = [
#     '467..114..',
#     '...*......',
#     '..35..633.',
#     '......#...',
#     '617*......',
#     '.....+.58.',
#     '..592.....',
#     '......755.',
#     '...$.*....',
#     '.664.598..'
# ]
#532870

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+..58
# ..592.....
# ......755.
# ...$.*....
# .664.598..

def HasSymbolAround(data, startIndexX, endIndexX, indexY):
    symbolClose = False

    x = startIndexX - 1
    y = indexY - 1
    if y >= 0:
        while x < len(data[indexY]) and x <= endIndexX:
            if x >= 0:
                symbolClose |= IsSymbol(data[y][x])
            x += 1

    x = startIndexX - 1
    y = indexY + 1
    if y < len(data):
        while x < len(data[indexY]) and x <= endIndexX:
            if x >= 0:
                hasSymbol = IsSymbol(data[y][x])
                symbolClose |= hasSymbol
            x += 1

    x = startIndexX - 1
    if x > 0:
        symbolClose |= IsSymbol(data[indexY][x])
    x = endIndexX
    if x < len(data[indexY]):
        symbolClose |= IsSymbol(data[indexY][x])

    return symbolClose
    

def IsSymbol(character):
    return character not in numbers and character != DOT

sum = 0


for y in range(len(data)):
# for y in range(2):
    line = data[y]
    x = 0
    tempChar = f''
    tempStartIndex = -1

    while x <= len(line):

        if x == len(line):
            if len(tempChar) > 0:
                if HasSymbolAround(data, tempStartIndex, x, y):
                    sum += int(tempChar)
                    print(tempChar)
                else:
                    print("NOT " + tempChar)

            tempStartIndex = -1
            tempChar = f''

        elif line[x] in numbers:
            if tempStartIndex == -1:
                tempStartIndex = x

            tempChar += line[x]
            
        else:
            if len(tempChar) > 0:
                #search for Symbol
                if HasSymbolAround(data, tempStartIndex, x, y):
                    sum += int(tempChar)
                    print(tempChar)
                else:
                    print("NOT " + tempChar)

            tempStartIndex = -1
            tempChar = f''

        x += 1


print(sum)
