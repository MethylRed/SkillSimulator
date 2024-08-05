# -*- coding: utf-8 -*-

import pulp
import csv

# 線形計画問題の定義
# 最大化問題を解く
problem = pulp.LpProblem('test', pulp.LpMaximize)


# 係数行列,個数ベクトル,装備カテゴリ配列を宣言
equip = [[],[],[],[],[],[]]
numEquip = [[],[],[],[],[],[]]
equipCategory = ['head', 'body', 'arm', 'wst', 'leg', 'charm']
with open('./skillName.csv', mode='r', encoding='utf-8') as file:
    skillName = list(csv.reader(file))

# 装備のデータを読み込む
# 先頭の行(見出し)を削除
for i in range(len(equipCategory)):
    with open('./data/' + equipCategory[i] + '.csv', mode='r', encoding='utf-8') as file:
        equip[i] = list(csv.reader(file))
    del equip[i][0]
with open('./data/deco.csv', mode='r', encoding='utf-8') as file:
    deco = list(csv.reader(file))
del deco[0]

# 個数ベクトルを初期化
for i in range(len(equipCategory)):
    numEquip[i] = [0] * len(equip[i])
numDeco = [0] * (len(deco))

# 個数ベクトルの定義
# 防具・護石は1つしか装備できない
for i in range(len(equipCategory)):
    for j in range(len(numEquip[i])):
        numEquip[i][j] = pulp.LpVariable('numEquip'+str(i)+','+str(j), cat=pulp.LpBinary)
for i in range(len(deco)):
    numDeco[i] = pulp.LpVariable('numDeco'+str(i), lowBound=0, upBound=7, cat=pulp.LpInteger)

# 係数行列*個数ベクトルの積:結果ベクトルの初期化
y = [0] * (len(equip[0][0])-1)

# 結果ベクトルの計算
for i in range(len(y)):
    for j in range(len(deco)):
        y[i] += int(deco[j][i+1]) * numDeco[i]
        print(y[6])
for i in range(len(y)):
    for j in range(len(equipCategory)):
        for k in range(len(equip[j])):
            y[i] += int(equip[j][k][i+1]) * numEquip[j][k]


# 防御を最適化
problem += y[10]


# ここに制約条件を書く
# 防具は各部位1個まで装備可能
for i in range(6):
    problem += 0 <= y[i] <= 1
problem += 0 <= y[6]
problem += 0 <= y[7]
problem += 0 <= y[8]
problem += 0 <= y[9]
problem += 0 <= y[11]
problem += 0 <= y[12]
problem += 0 <= y[13]
problem += 0 <= y[14]
problem += 5 <= y[15]
problem += 0 <= y[16]
problem += 0 <= y[17]
problem += 0 <= y[18]
problem += 0 <= y[19]
problem += 0 <= y[20]
problem += 0 <= y[21]
problem += 0 <= y[22]
problem += 0 <= y[23]
problem += 0 <= y[24]
problem += 0 <= y[25]
problem += 0 <= y[26]
problem += 0 <= y[27]
problem += 0 <= y[28]
problem += 0 <= y[29]
problem += 0 <= y[30]
problem += 0 <= y[31]
problem += 0 <= y[32]
problem += 0 <= y[33]
problem += 0 <= y[34]
problem += 0 <= y[35]
problem += 0 <= y[36]
problem += 0 <= y[37]
problem += 0 <= y[38]
problem += 0 <= y[39]
problem += 0 <= y[40]
problem += 0 <= y[41]
problem += 0 <= y[42]
problem += 0 <= y[43]
problem += 0 <= y[44]
problem += 0 <= y[45]
problem += 0 <= y[46]
problem += 0 <= y[47]
problem += 0 <= y[48]
problem += 0 <= y[49]
problem += 0 <= y[50]
problem += 0 <= y[51]
problem += 0 <= y[52]
problem += 0 <= y[53]
problem += 0 <= y[54]
problem += 0 <= y[55]
problem += 0 <= y[56]
problem += 0 <= y[57]
problem += 0 <= y[58]
problem += 0 <= y[59]
problem += 0 <= y[60]
problem += 0 <= y[61]
problem += 0 <= y[62]
problem += 0 <= y[63]
problem += 0 <= y[64]
problem += 0 <= y[65]
problem += 0 <= y[66]
problem += 0 <= y[67]
problem += 0 <= y[68]
problem += 0 <= y[69]
problem += 0 <= y[70]
problem += 0 <= y[71]
problem += 0 <= y[72]
problem += 0 <= y[73]
problem += 0 <= y[74]
problem += 0 <= y[75]
problem += 0 <= y[76]
problem += 0 <= y[77]
problem += 0 <= y[78]
problem += 0 <= y[79]
problem += 0 <= y[80]
problem += 0 <= y[81]
problem += 0 <= y[82]
problem += 0 <= y[83]
problem += 0 <= y[84]
problem += 0 <= y[85]
problem += 0 <= y[86]
problem += 0 <= y[87]
problem += 0 <= y[88]
problem += 0 <= y[89]
problem += 0 <= y[90]
problem += 0 <= y[91]
problem += 0 <= y[92]
problem += 0 <= y[93]
problem += 0 <= y[94]
problem += 0 <= y[95]
problem += 0 <= y[96]
problem += 0 <= y[97]
problem += 0 <= y[98]
problem += 0 <= y[99]
problem += 0 <= y[100]
problem += 0 <= y[101]
problem += 0 <= y[102]
problem += 0 <= y[103]
problem += 0 <= y[104]
problem += 0 <= y[105]
problem += 0 <= y[106]
problem += 0 <= y[107]
problem += 0 <= y[108]
problem += 0 <= y[109]
problem += 0 <= y[110]
problem += 0 <= y[111]
problem += 0 <= y[112]
problem += 0 <= y[113]
problem += 0 <= y[114]
problem += 0 <= y[115]
problem += 0 <= y[116]
problem += 0 <= y[117]
problem += 0 <= y[118]
problem += 0 <= y[119]
problem += 0 <= y[120]
problem += 0 <= y[121]
problem += 0 <= y[122]
problem += 0 <= y[123]
problem += 0 <= y[124]
problem += 0 <= y[125]
problem += 0 <= y[126]
problem += 0 <= y[127]
problem += 0 <= y[128]
problem += 0 <= y[129]
problem += 0 <= y[130]
problem += 0 <= y[131]
problem += 0 <= y[132]
problem += 0 <= y[133]
problem += 0 <= y[134]
problem += 0 <= y[135]
problem += 0 <= y[136]
problem += 0 <= y[137]
problem += 0 <= y[138]
problem += 0 <= y[139]
problem += 0 <= y[140]
problem += 0 <= y[141]
problem += 0 <= y[142]
problem += 0 <= y[143]
problem += 0 <= y[144]
problem += 0 <= y[145]
problem += 0 <= y[146]
problem += 0 <= y[147]
problem += 0 <= y[148]
problem += 0 <= y[149]
problem += 0 <= y[150]
problem += 0 <= y[151]
problem += 0 <= y[152]
problem += 0 <= y[153]
problem += 0 <= y[154]
problem += 0 <= y[155]
problem += 0 <= y[156]
problem += 0 <= y[157]
problem += 0 <= y[158]
problem += 0 <= y[159]
problem += 0 <= y[160]
problem += 0 <= y[161]
problem += 0 <= y[162]
problem += 0 <= y[163]
problem += 0 <= y[164]
problem += 0 <= y[165]
problem += 0 <= y[166]
problem += 0 <= y[167]
problem += 0 <= y[168]
problem += 0 <= y[169]
problem += 0 <= y[170]
problem += 0 <= y[171]
problem += 0 <= y[172]
problem += 0 <= y[173]
problem += 0 <= y[174]
problem += 0 <= y[175]
problem += 0 <= y[176]
problem += 0 <= y[177]
problem += 0 <= y[178]
problem += 0 <= y[179]
problem += 0 <= y[180]
problem += 4 <= y[181]
problem += 0 <= y[182]
problem += 0 <= y[183]
problem += 0 <= y[184]
problem += 0 <= y[185]
problem += 0 <= y[186]
problem += 0 <= y[187]
problem += 0 <= y[188]
problem += 0 <= y[189]
problem += 0 <= y[190]
problem += 0 <= y[191]
problem += 0 <= y[192]
problem += 0 <= y[193]
problem += 0 <= y[194]
problem += 0 <= y[195]
problem += 0 <= y[196]
problem += 0 <= y[197]
problem += 0 <= y[198]
problem += 0 <= y[199]
problem += 0 <= y[200]
problem += 0 <= y[201]
problem += 0 <= y[202]
problem += 0 <= y[203]
problem += 0 <= y[204]
problem += 0 <= y[205]
problem += 0 <= y[206]
problem += 0 <= y[207]
problem += 0 <= y[208]
problem += 0 <= y[209]
problem += 0 <= y[210]
status = problem.solve()

print(pulp.LpStatus[status])
# for i in range(6):
#     for j in range(len(numEquip[i])):
#         if numEquip[i][j].value() != 0:
#             print(equip[i][j][0] + "*" + str(numEquip[i][j].value()))
# print(int(y[10].value()))
# for i in range(11,len(y)):
#     # if y[i].value() != 0:
#         print(str(skillName[i-11][0]) + 'Lv' + str(int(y[i].value())))

# for i in range(len(numDeco)):
#     if numDeco[i].value() != None:
#         print(deco[i][0] + "*" + str(int(numDeco[i].value())))

# print(y[6].value())
# print(y[7].value())
# print(y[8].value())
# print(y[9].value())

# print(numDeco[0].value())
