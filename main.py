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

# スキル条件を設定したCSVファイルを読み込む
with open('./skillCondition.csv', mode='r', encoding='utf-8') as file:
    skillCondition = list(csv.reader(file))

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

# 結果ベクトル(=係数行列*個数ベクトルの積)の初期化
y = [0] * (len(equip[0][0])-1)

# 結果ベクトルの計算
for i in range(len(y)):
    for j in range(len(deco)):
        y[i] += int(deco[j][i+1]) * numDeco[j]
for i in range(len(y)):
    for j in range(len(equipCategory)):
        for k in range(len(equip[j])):
            y[i] += int(equip[j][k][i+1]) * numEquip[j][k]


# 防御を最適化
problem += y[10]

# ここに制約条件を書く
# 防具・護石は1個まで装備可能
for i in range(6):
    problem += 0 <= y[i] <= 1
# 装飾品スロットは不足してはいけない
for i in range(4):
    problem += 0 <= y[i+6]

# スキル条件
for i in range(len(skillCondition)):
    problem += int(skillCondition[i][1]) <= y[i+11], 'skill'+str(i)

status = problem.solve(pulp.PULP_CBC_CMD(msg = False))

slot = [0] * 4
mtSlot = [0] * 4
decoSlot = [0] * 4
mtDecoSlot = [0] * 4
selectedEquipIndex = [0] * 6
selectedDecoIndex = []

print(pulp.LpStatus[status])
if pulp.LpStatus[status] == "Optimal":
    for i in range(6):
        for j in range(len(numEquip[i])):
            if numEquip[i][j].value() != 0:
                print(equip[i][j][0] + " * " + str(int(numEquip[i][j].value())))
                selectedEquipIndex[i] = j
    print(int(y[10].value()))
    for i in range(11,len(y)):
        if y[i].value() != 0:
            print(str(skillCondition[i-11][0]) + 'Lv' + str(int(y[i].value())))
    for i in range(len(numDeco)):
        if numDeco[i].value() != 0:
            print(deco[i][0] + " * " + str(int(numDeco[i].value())))
            selectedDecoIndex.append(i)

    for i in range(5):
        for j in range(4):
            mtSlot[j] += int(equip[i][selectedEquipIndex[i]][j+7])
    slot[3] = mtSlot[3]
    slot[2] = mtSlot[2] - mtSlot[3]
    slot[1] = mtSlot[1] - mtSlot[2]
    slot[0] = mtSlot[0] - mtSlot[1]

    for i in range(len(selectedDecoIndex)):
        for j in range(4):
            mtDecoSlot[j] += abs(int(deco[selectedDecoIndex[i]][j+7])) * int(numDeco[selectedDecoIndex[i]].value())
    decoSlot[3] = mtDecoSlot[3]
    decoSlot[2] = mtDecoSlot[2] - mtDecoSlot[3]
    decoSlot[1] = mtDecoSlot[1] - mtDecoSlot[2]
    decoSlot[0] = mtDecoSlot[0] - mtDecoSlot[1]

    if (slot[0] - decoSlot[0]) > 0:
        print("Lv1スロット * " + str(slot[0] - decoSlot[0]))
    else:
        slot[1] -= abs(slot[0] - decoSlot[0])
    if (slot[1] - decoSlot[1]) > 0:
        print("Lv2スロット * " + str(slot[1] - decoSlot[1]))
    else:
        slot[2] -= abs(slot[1] - decoSlot[1])
    if (slot[2] - decoSlot[0]) > 0:
        print("Lv3スロット * " + str(slot[2] - decoSlot[2]))
    else:
        slot[3] -= abs(slot[2] - decoSlot[2])
    if (slot[3] - decoSlot[3]) > 0:
        print("Lv4スロット * " + str(slot[3] - decoSlot[3]))
    
    # 追加スキル検索
    print("\n追加スキル検索を実行しますか? y/n")
    input = input()
    if input == 'y':
        for i in range(len(skillCondition)):
            del problem.constraints['skill'+str(i)]
            problem += (int(skillCondition[i][1])+1) <= y[i+11], 'skill'+str(i)
            if i != 0:
                del problem.constraints['skill'+str(i-1)]
                problem += (int(skillCondition[i-1][1])) <= y[i-1+11], 'skill'+str(i-1)

            status = problem.solve(pulp.PULP_CBC_CMD(msg = False))

            if pulp.LpStatus[status] == "Optimal":
                print("追加スキル検索:" + skillCondition[i][0] + "+1")
                # slot = [0] * 4
                # mtSlot = [0] * 4
                # decoSlot = [0] * 4
                # mtDecoSlot = [0] * 4
                # selectedEquipIndex = [0] * 6
                # selectedDecoIndex = []
                # for i in range(6):
                #     for j in range(len(numEquip[i])):
                #         if numEquip[i][j].value() != 0:
                #             print(equip[i][j][0] + " * " + str(int(numEquip[i][j].value())))
                #             selectedEquipIndex[i] = j
                # print(int(y[10].value()))
                # for i in range(11,len(y)):
                #     if y[i].value() != 0:
                #         print(str(skillCondition[i-11][0]) + 'Lv' + str(int(y[i].value())))
                # for i in range(len(numDeco)):
                #     if numDeco[i].value() != 0:
                #         print(deco[i][0] + " * " + str(int(numDeco[i].value())))
                #         selectedDecoIndex.append(i)

                # for i in range(5):
                #     for j in range(4):
                #         mtSlot[j] += int(equip[i][selectedEquipIndex[i]][j+7])
                # slot[3] = mtSlot[3]
                # slot[2] = mtSlot[2] - mtSlot[3]
                # slot[1] = mtSlot[1] - mtSlot[2]
                # slot[0] = mtSlot[0] - mtSlot[1]

                # for i in range(len(selectedDecoIndex)):
                #     for j in range(4):
                #         mtDecoSlot[j] += abs(int(deco[selectedDecoIndex[i]][j+7])) * int(numDeco[selectedDecoIndex[i]].value())
                # decoSlot[3] = mtDecoSlot[3]
                # decoSlot[2] = mtDecoSlot[2] - mtDecoSlot[3]
                # decoSlot[1] = mtDecoSlot[1] - mtDecoSlot[2]
                # decoSlot[0] = mtDecoSlot[0] - mtDecoSlot[1]

                # if (slot[0] - decoSlot[0]) > 0:
                #     print("Lv1スロット * " + str(slot[0] - decoSlot[0]))
                # else:
                #     slot[1] -= abs(slot[0] - decoSlot[0])
                # if (slot[1] - decoSlot[1]) > 0:
                #     print("Lv2スロット * " + str(slot[1] - decoSlot[1]))
                # else:
                #     slot[2] -= abs(slot[1] - decoSlot[1])
                # if (slot[2] - decoSlot[0]) > 0:
                #     print("Lv3スロット * " + str(slot[2] - decoSlot[2]))
                # else:
                #     slot[3] -= abs(slot[2] - decoSlot[2])
                # if (slot[3] - decoSlot[3]) > 0:
                #     print("Lv4スロット * " + str(slot[3] - decoSlot[3]))


