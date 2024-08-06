# -*- coding: utf-8 -*-

import pulp
import csv
# import sys

# 線形計画問題の定義
# 最大化問題を解く
problem = pulp.LpProblem('test', pulp.LpMaximize)


# 係数行列,個数ベクトル,装備カテゴリ配列
equip = [[],[],[],[],[],[]]
numEquip = [[],[],[],[],[],[]]
equipCategory = ['head', 'body', 'arm', 'wst', 'leg', 'charm']

# 解の保存用配列
resEquipIndex = [0] * 6
resDecoIndex = []


# スキル条件を設定したCSVファイルを読み込む
with open('./skillCondition.csv', mode='r', encoding='utf-8') as file:
    skillCondition = list(csv.reader(file))
del skillCondition[0]

# 装備のデータを読み込む
# 先頭の行(見出し)を削除
for i in range(len(equipCategory)):
    with open('./data/' + equipCategory[i] + '.csv', mode='r', encoding='utf-8') as file:
        equip[i] = list(csv.reader(file))
    del equip[i][0]
with open('./data/deco.csv', mode='r', encoding='utf-8') as file:
    deco = list(csv.reader(file))
del deco[0]
with open('./haveDeco.csv', mode='r', encoding='utf-8') as file:
    haveDeco = list(csv.reader(file))
del haveDeco[0]
with open('./excludeEquip.csv', mode='r', encoding='utf-8') as file:
    excludeEquip = list(csv.reader(file))
del excludeEquip[0]
with open('./weapon.csv', mode='r', encoding='utf-8') as file:
    weapon = list(csv.reader(file))
del weapon[0]

# 個数ベクトルを初期化
for i in range(len(equipCategory)):
    numEquip[i] = [0] * len(equip[i])
numDeco = [0] * (len(deco))

# 個数ベクトルの定義
# 防具・護石
for i in range(len(equipCategory)):
    k = 0
    for j in range(len(numEquip[i])):
        # 防具
        if i < 5:
            # 存在しない装備はスキップ
            while int(excludeEquip[j+k][i+1]) == -1:
                k += 1
            # 除外しない場合
            if int(excludeEquip[j+k][i+1]) == 0:
                numEquip[i][j] = pulp.LpVariable('numEquip'+str(i)+','+str(j), cat=pulp.LpBinary)
            # 除外する場合
            elif int(excludeEquip[j+k][i+1]) == 1:
                numEquip[i][j] = pulp.LpVariable('numEquip'+str(i)+','+str(j), 
                                                 lowBound=0, upBound=0, cat=pulp.LpInteger)
            else:
                exit("excludeEquip.csvに0または1以外の文字が含まれています。")
        # 護石
        else:
            numEquip[i][j] = pulp.LpVariable('numEquip'+str(i)+','+str(j), cat=pulp.LpBinary)

# 装飾品
for i in range(len(deco)):
    numDeco[i] = pulp.LpVariable('numDeco'+str(i), lowBound=0, upBound=int(haveDeco[i][1]), cat=pulp.LpInteger)


# 結果ベクトル(=係数行列*個数ベクトルの積)の初期化
y = [0] * (len(equip[0][0])-1)

# 結果ベクトルの計算
for i in range(len(y)):
    for j in range(len(equipCategory)):
        for k in range(len(equip[j])):
            y[i] += int(equip[j][k][i+1]) * numEquip[j][k]
for i in range(len(y)):
    for j in range(len(deco)):
        # print(deco[j][i+1])
        y[i] += int(deco[j][i+1]) * numDeco[j]


# 防御を最適化
problem += y[10]

# ここに制約条件を書く
# 防具・護石は1個まで装備可能
for i in range(6):
    problem += 0 <= y[i] <= 1
# 装飾品スロットは不足してはいけない
for i in range(4):
    problem += -int(weapon[0][i+6]) <= y[i+6]

# スキル条件
# 武器スキル分を引く
for i in range(len(skillCondition)):
    problem += (int(skillCondition[i][1]) - int(weapon[0][i+16])) <= y[i+16], 'skill'+str(i)


# 最適化問題を解く
# 検索回数
# 非負整数以外は弾く
while (True):
    string = input("検索回数を入力してください。(最大50) ")
    if string.isdecimal(): break
    print("非負整数を入力してください。")
numSearch = int(string)
if numSearch > 50: numSearch = 50
count = 0
while (True):
    status = problem.solve(pulp.PULP_CBC_CMD(msg = False))

    # 解があるand検索回数が指定値以下なら解を表示
    if (pulp.LpStatus[status] == "Optimal") & (count < min(numSearch,50)):
        # 防具・護石の表示
        for i in range(6):
            for j in range(len(numEquip[i])):
                if numEquip[i][j].value() != 0:
                    print(equip[i][j][0] + " * " + str(int(numEquip[i][j].value())))
                    resEquipIndex[i] = j
        # 防御力,属性耐性の表示
        for i in range(10,16):
            print(int(y[i].value()), end=', ')
        print("\n")

        # 発動スキルの表示
        for i in range(16,len(y)):
            if y[i].value() != 0:
                print(str(skillCondition[i-16][0]) + 'Lv' + str(int(y[i].value())+int(weapon[0][i])))

        # 必要な装飾品の表示
        for i in range(len(numDeco)):
            if numDeco[i].value() != 0:
                print(deco[i][0] + " * " + str(int(numDeco[i].value())))
                resDecoIndex.append(i)

        # 余りスロットの表示
        y6 = int(y[6].value()+int(weapon[0][6]))
        y7 = int(y[7].value()+int(weapon[0][7]))
        y8 = int(y[8].value()+int(weapon[0][8]))
        y9 = int(y[9].value()+int(weapon[0][9]))
        print("Lv1スロット余り * " + str(y6 - min(y6,y7)))
        print("Lv2スロット余り * " + str(min(y6,y7) - min(y6,y7,y8)))
        print("Lv3スロット余り * " + str(min(y6,y7,y8) - min(y6,y7,y8,y9)))
        print("Lv4スロット余り * " + str(min(y6,y7,y8,y9)))
        print("\n")

        # 複数検索のための条件として同じ防具・護石の組み合わせを除外する
        resExcluded = 0
        for i in range(6):
            resExcluded += numEquip[i][resEquipIndex[i]]
        problem += resExcluded <= 5, 'multiSearch'+str(count)

        count += 1
    else:
        break




# 追加スキル検索
if count > 0:
    print("\n追加スキル検索を実行しますか? y/n")
    input = input()
    if input == 'y':
        # 複数検索条件をすべて削除
        for i in range(count):
            del problem.constraints['multiSearch'+str(count-1)]
        # 全スキルから一つだけLvを+1して問題を解く
        for i in range(len(skillCondition)):
            j = 1
            while (True):
                del problem.constraints['skill'+str(i)]
                problem += (int(skillCondition[i][1])+j) <= y[i+16], 'skill'+str(i)
                if (i != 0) & (j == 1):
                    del problem.constraints['skill'+str(i-1)]
                    problem += (int(skillCondition[i-1][1])) <= y[i-1+16], 'skill'+str(i-1)

                # +jして上限を超える場合はスキップ
                if int(skillCondition[i][1])+j <= int(skillCondition[i][3]):
                    status = problem.solve(pulp.PULP_CBC_CMD(msg = False))

                    if pulp.LpStatus[status] == "Optimal":
                        print("追加スキル検索:" + skillCondition[i][0] + "Lv" + str(int(skillCondition[i][1])+j))
                else:
                    break
                j += 1