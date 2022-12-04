"""
@author: laura.zikovic
"""
#Day:
n = 3

input_data = open(f"Inputday{n}.txt").read().strip().split("\n")

inter, priority1, inter2, priority2, num_bags = [], [], [], [], 3

for i in input_data:
    first = i[:len(i) // 2]
    second = i[len(i) // 2:]
    inter += set(first).intersection(second)

for i in range(0, len(input_data), num_bags):
    inter2 += set(input_data[i]).intersection(input_data[i+1], input_data[i+2])

#Skratiti def
for i in inter:
    if (i.islower()) == True:
        priority1.append((ord(i) - 97 + 1))     #"A" = 65, "a"= 97
    else:
        priority1.append((ord(i) - 65 + 27))

for i in inter2:
    if (i.islower()) == True:
        priority2.append((ord(i) - 97 + 1))     #"A" = 65, "a"= 97
    else:
        priority2.append((ord(i) - 65 + 27))  
   
print(sum(priority1), sum(priority2))

#Notes: Auto input from url:
#import requests
#html_data = f"https://adventofcode.com/2022/day/{n}/input"
#input_data = requests.get(html_data)
#print(input_data.text)   
#I tried alos with cookies, webdriver...
#Puzzle inputs differ by user. Please log in to get your puzzle input. 

# Source: https://note.nkmk.me/en/python-chr-ord-unicode-code-point/