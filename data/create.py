# -*- coding: utf-8 -*-
import csv

fname = "leg"

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

    a = [reader[i][0],
        1 if 'head' in file.name else 0,
        1 if 'body' in file.name else 0,
        1 if 'arm' in file.name else 0,
        1 if 'wst' in file.name else 0,
        1 if 'leg' in file.name else 0,
        1 if 'charm' in file.name else 0,
        s1,s2,s3,s4,
        int(reader[i][8]),
        int(reader[i][9]),
        int(reader[i][10]),
        int(reader[i][11]),
        int(reader[i][12]),
        int(reader[i][13]),
        ]



    skill = [0] * len(r)
    for j in range(len(r)):
        if reader[i][14] == r[j][0]:
            skill[j] = int(reader[i][15])
        if reader[i][16] == r[j][0]:
            skill[j] = int(reader[i][17])
        if reader[i][18] == r[j][0]:
            skill[j] = int(reader[i][19])
        if reader[i][20] == r[j][0]:
            skill[j] = int(reader[i][21])
        if reader[i][22] == r[j][0]:
            skill[j] = int(reader[i][23])

    a += skill

    with open('./data/'+fname+'.csv', mode='a', encoding='utf-8') as file:
        for s in a:
            file.write(str(s) + ",")
        file.write("\n")
