# -*- coding: utf-8 -*-
import csv

fname = "charm"

with open('./skillCondition.csv', mode='r', encoding='utf-8') as file:
    r = list(csv.reader(file))

index = ["name", "head", "body", "arm", "wst", "leg", "charm",
         "NumMoreThanLv1Slot",
         "NumMoreThanLv2Slot",
         "NumMoreThanLv3Slot",
         "NumMoreThanLv4Slot",
         "Defense",
         "Fire Res",
         "Water Res",
         "Thunder Res",
         "Ice Res",
         "Dragon Res",
         ]

for s in r:
    index.append(s[0])

with open('./data2/'+fname+'.csv', mode='w', encoding='utf-8') as file:
    for s in index:
        file.write(str(s) + ",")
    file.write("\n")

with open('./ext/'+fname+'.csv', mode='r', encoding='utf-8') as file:
    reader = list(csv.reader(file))

for i in range(1,len(reader)):
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0

    for j in range(3,6):
        if reader[i][j] == '1':
            s1 += 1
        elif reader[i][j] == '2':
            s1 += 1
            s2 += 1
        elif reader[i][j] == '3':
            s1 += 1
            s2 += 1
            s3 += 1
        elif reader[i][j] == '4':
            s1 += 1
            s2 += 1
            s3 += 1
            s4 += 1


    a = [reader[i][0],0,0,0,0,0,1,0,0,0,0,
         0,
         0,0,0,0,0,
        ]

    skill = [0] * len(r)
    for j in range(len(r)):
        if reader[i][3] == r[j][0]:
            skill[j] = int(reader[i][4])
        if reader[i][5] == r[j][0]:
            skill[j] = int(reader[i][6])

    a += skill

    with open('./data2/'+fname+'.csv', mode='a', encoding='utf-8') as file:
        for s in a:
            file.write(str(s) + ",")
        file.write("\n")