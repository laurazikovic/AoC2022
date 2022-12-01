"""
@author: laura.zikovic
"""
input_data = open("Inputday1.txt").read().strip().split("\n")

calories = 0 
cal_pat = []
for i in input_data:
    if i == '':
        cal_pat.append(calories)
        calories = 0
    else:
        calories += int(i)
cal_pat.append(calories)

print(max(cal_pat),sum(sorted(cal_pat)[-3:]))
