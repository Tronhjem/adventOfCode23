import requests
from datetime import datetime
from sys import argv

def WriteFileForDay(day, coookieToPass = ''):
    headers = {}
    cookie = '_ga=GA1.2.703571093.1699009238; _gid=GA1.2.719032647.1700662195; session=53616c7465645f5f9165ba213433084ee51f8927b2fba2db1e1ba5e6af031c0653b80fdffddae89a42146758754d642c23b8141fa34097483f0e0075b8497806; _ga_MHSNPJKWC7=GS1.2.1700662195.3.1.1700663553.0.0.0'
    
    if (len(coookieToPass) > 0):
        headers['Cookie'] = coookieToPass
    else:
        headers['Cookie'] = cookie
    
    response = requests.get (f'https://adventofcode.com/2023/day/{str(day)}/input', headers=headers)

    if(response.status_code == 200):
        with open(f'./data/{day}.txt', "w+") as file:
            file.write(response.content.decode())

        print("Wrote file " f'{day}.txt')
    else:
        print(f'Bad Response {response}')


def MakeArrayFromFile(file):
    with open(file, 'r') as file:
        output = file.readlines()
    for x in range(len(output)):
        output[x] = output[x].replace('\n', '')
    return output 


def MakeLinesFromStringToInt(lines):
    for x in range(len(lines)):
        try:
            lines[x] = int(lines[x])
        except:
            continue
    return lines


if __name__ == "__main__":
    day = datetime.today().strftime('%d')
    if day[0] == '0':
        day = day[1]
    
    cookie = argv[1]
    # cookie = 'session=53616c7465645f5f142775de060dd5d1a73f5c9830decf5353273581f0c5703898444b20bab2b9f58703b1d5ea22761f597cf57fe25de02bb863c591f63b8760'
    if len(cookie) > 1:
        WriteFileForDay(day, cookie)
    else:
        WriteFileForDay(day)

    
    
