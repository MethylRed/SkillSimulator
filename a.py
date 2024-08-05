import csv

with open('./skillName.csv', mode='r', encoding='utf-8') as file:
    skillName = list(csv.reader(file))

for i in range(11,211):
    print("problem += int(skillName[" + str(i-11) + "][1]) <= y[" + str(i) + "]\t# " + skillName[i-11][0])