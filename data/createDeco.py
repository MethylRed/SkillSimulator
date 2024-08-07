# -*- coding: utf-8 -*-
import csv

fname = "deco"

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

with open('./data/'+fname+'.csv', mode='w', encoding='utf-8') as file:
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

    if reader[i][2] == '1':
        s1 -= 1
    elif reader[i][2] == '2':
        s1 -= 1
        s2 -= 1
    elif reader[i][2] == '3':
        s1 -= 1
        s2 -= 1
        s3 -= 1
    elif reader[i][2] == '4':
        s1 -= 1
        s2 -= 1
        s3 -= 1
        s4 -= 1


    a = [reader[i][0],0,0,0,0,0,0,
        s1,s2,s3,s4,
        0,
        0,0,0,0,0
        ]


    skill = [0] * len(r)
    for j in range(len(r)):
        if reader[i][4] == r[j][0]:
            skill[j] = int(reader[i][5])
        if reader[i][6] == r[j][0]:
            skill[j] = int(reader[i][7])

    a += skill

    with open('./data/'+fname+'.csv', mode='a', encoding='utf-8') as file:
        for s in a:
            file.write(str(s) + ",")
        file.write("\n")