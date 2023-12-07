import re

with open('data/6.txt', 'r') as file:
    data = file.readlines()

for line in range(len(data)):
    data[line] = data[line].replace('\n', '')



def GetTotalDistance(timeTotal, timeHeld):
    return (timeTotal - timeHeld) * timeHeld

# (time - timeHeld) * timeHeld 
#  (7 - 2) * 2 = 10
#  (7 - 3) * 3 = 12


# times = list(map(int, re.findall(r'\d+', data[0])))

# distance = list(map(int, re.findall(r'\d+', data[1])))

#day two mod
times = [int(data[0].split(':')[1].replace(' ', ''))]
distance = [int(data[1].split(':')[1].replace(' ', ''))]

records = []
index = 0
for time in times:
    timeHeld = 0
    localRecord = 0
    while timeHeld < time:
        totalDistance = GetTotalDistance(time, timeHeld)
        if totalDistance > distance[index]:
            localRecord += 1
        timeHeld += 1
    records.append(localRecord)
    index += 1

sum = 1
for y in records:
    sum *= y
print(sum)



