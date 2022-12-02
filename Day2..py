"""
Created on Fri Dec  2 08:46:16 2022

@author: laura.zikovic
"""

input_data = open("Inputday2.txt").read().split("\n")

total = 0 
for i in input_data:
    if i == 'A X':
        total += (3+1)
    elif i == 'A Y':
        total += (6+2)
    elif i == 'A Z':
        total += (0+3)
    elif i == 'B X':
        total += (0+1)
    elif i == 'B Y':
        total += (3+2)
    elif i == 'B Z':
        total += (6+3)
    elif i == 'C X':
        total += (6+1)
    elif i == 'C Y':
        total += (0+2)
    elif i == 'C Z':
        total += (3+3)
        
total2 = 0 
for i in input_data:
    if i == 'A X':
        total2 += (3+0)
    elif i == 'A Y':
        total2 += (1+3)
    elif i == 'A Z':
        total2 += (2+6)
    elif i == 'B X':
        total2 += (1+0)
    elif i == 'B Y':
        total2 += (2+3)
    elif i == 'B Z':
        total2 += (3+6)
    elif i == 'C X':
        total2 += (2+0)
    elif i == 'C Y':
        total2 += (3+3)
    elif i == 'C Z':
        total2 += (1+6)

print(total, total2)

