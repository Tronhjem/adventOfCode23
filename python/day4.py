
with open("../data/4.txt") as file:
    data = file.readlines()


for i in range(len(data)):
    data[i] = data[i].replace('\n','')

#first 
# totalScore = 0
# for x in range(len(data)):
#     games = data[x].split(':')[1].split('|')
    
#     winNumbers = []
#     myNumbers = []
#     for x in games[0].split(' '):
#         try:
#             winNumbers.append(int(x))
#         except:
#             continue

#     for x in games[1].split(' '):
#         try:
#             myNumbers.append(int(x))
#         except:
#             continue

#     wins = 0
#     score = 0
#     for number in myNumbers:
#         if number in winNumbers:
#             wins += 1
    
#     if wins > 0:
#         if wins == 1:
#             score = 1
#         else:
#             score = pow(2,wins - 1)
#         totalScore += score

# print(totalScore)


#second
totalScore = 0
cardIndex = [1] * len(data)

for x in range(len(data)):
    print(x)
    games = data[x].split(':')[1].split('|')
    
    winNumbers = []
    myNumbers = []
    for winNumber in games[0].split(' '):
        try:
            winNumbers.append(int(winNumber))
        except:
            continue

    for myNumber in games[1].split(' '):
        try:
            myNumbers.append(int(myNumber))
        except:
            continue

    for card in range(cardIndex[x]):
        wins = 0
        for number in myNumbers:
            if number in winNumbers:
                wins += 1
        
        nextIndex = x + 1
        for y in range(wins):
            if y + nextIndex < len(cardIndex):
                cardIndex[y + nextIndex] += 1


sum = 0
for num in cardIndex:
    sum += num
    
    
print(sum)