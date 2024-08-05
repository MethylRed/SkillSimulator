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
        numEquip[i][j] = pulp.LpVariable('numEquip['+str(i)+']['+str(j)+']', cat=pulp.LpBinary)
for i in range(len(deco)):
    numDeco[i] = pulp.LpVariable('numdeco'+str(i), 0, 7, pulp.const.LpInteger)

# 係数行列*個数ベクトルの積:結果ベクトルの初期化
y = [0] * (len(equip[0][0])-1)

# 結果ベクトルの計算
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
problem += y[200] >= 4
problem += y[41] >= 2

status = problem.solve()

print(pulp.LpStatus[status])
for i in range(6):
    for j in range(len(numEquip[i])):
        if numEquip[i][j].value() != 0:
            print(equip[i][j][0])
print(int(y[10].value()))
for i in range(11,len(y)):
    if y[i].value() != 0:
        print(str(skillName[i-11][0]) + 'Lv' + str(int(y[i].value())))
