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
        y[i] += int(deco[j][i+1]) * numDeco[j]
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

problem += int(skillName[0][1]) <= y[11]        # アイテム使用強化
problem += int(skillName[1][1]) <= y[12]        # 威嚇
problem += int(skillName[2][1]) <= y[13]        # 運搬の達人
problem += int(skillName[3][1]) <= y[14]        # オトモへの采配
problem += int(skillName[4][1]) <= y[15]        # ガード性能
problem += int(skillName[5][1]) <= y[16]        # 回避距離ＵＰ
problem += int(skillName[6][1]) <= y[17]        # 回避性能
problem += int(skillName[7][1]) <= y[18]        # 回復速度
problem += int(skillName[8][1]) <= y[19]        # 火事場力
problem += int(skillName[9][1]) <= y[20]        # 滑走強化
problem += int(skillName[10][1]) <= y[21]       # 雷属性攻撃強化
problem += int(skillName[11][1]) <= y[22]       # 雷耐性
problem += int(skillName[12][1]) <= y[23]       # 感知
problem += int(skillName[13][1]) <= y[24]       # 貫通弾・竜の一矢強化
problem += int(skillName[14][1]) <= y[25]       # 気絶耐性
problem += int(skillName[15][1]) <= y[26]       # キノコ大好き
problem += int(skillName[16][1]) <= y[27]       # 強化持続
problem += int(skillName[17][1]) <= y[28]       # クライマー
problem += int(skillName[18][1]) <= y[29]       # ＫＯ術
problem += int(skillName[19][1]) <= y[30]       # 研究者
problem += int(skillName[20][1]) <= y[31]       # 広域化
problem += int(skillName[21][1]) <= y[32]       # 攻撃
problem += int(skillName[22][1]) <= y[33]       # 氷属性攻撃強化
problem += int(skillName[23][1]) <= y[34]       # 氷耐性
problem += int(skillName[24][1]) <= y[35]       # こやし名人
problem += int(skillName[25][1]) <= y[36]       # 渾身
problem += int(skillName[26][1]) <= y[37]       # 昆虫標本の達人
problem += int(skillName[27][1]) <= y[38]       # 採集の達人
problem += int(skillName[28][1]) <= y[39]       # 寒さ耐性
problem += int(skillName[29][1]) <= y[40]       # 逆恨み
problem += int(skillName[30][1]) <= y[41]       # 散弾・剛射強化
problem += int(skillName[31][1]) <= y[42]       # 死中に活
problem += int(skillName[32][1]) <= y[43]       # しゃがみ移動速度ＵＰ
problem += int(skillName[33][1]) <= y[44]       # 弱点特効
problem += int(skillName[34][1]) <= y[45]       # ジャンプ鉄人
problem += int(skillName[35][1]) <= y[46]       # 集中
problem += int(skillName[36][1]) <= y[47]       # 瘴気環境適応
problem += int(skillName[37][1]) <= y[48]       # 瘴気耐性
problem += int(skillName[38][1]) <= y[49]       # 植生学
problem += int(skillName[39][1]) <= y[50]       # 導蟲反応距離ＵＰ
problem += int(skillName[40][1]) <= y[51]       # 睡眠属性強化
problem += int(skillName[41][1]) <= y[52]       # 睡眠耐性
problem += int(skillName[42][1]) <= y[53]       # 睡眠ビン追加
problem += int(skillName[43][1]) <= y[54]       # スタミナ急速回復
problem += int(skillName[44][1]) <= y[55]       # スタミナ奪取
problem += int(skillName[45][1]) <= y[56]       # スリンガー装填数ＵＰ
problem += int(skillName[46][1]) <= y[57]       # 整備
problem += int(skillName[47][1]) <= y[58]       # 精霊の加護
problem += int(skillName[48][1]) <= y[59]       # 閃光強化
problem += int(skillName[49][1]) <= y[60]       # 潜伏
problem += int(skillName[50][1]) <= y[61]       # 属性解放／装填拡張
problem += int(skillName[51][1]) <= y[62]       # 属性やられ耐性
problem += int(skillName[52][1]) <= y[63]       # 体術
problem += int(skillName[53][1]) <= y[64]       # 耐震
problem += int(skillName[54][1]) <= y[65]       # 体力回復量ＵＰ
problem += int(skillName[55][1]) <= y[66]       # 体力増強
problem += int(skillName[56][1]) <= y[67]       # 匠
problem += int(skillName[57][1]) <= y[68]       # 探索者の幸運
problem += int(skillName[58][1]) <= y[69]       # 力の解放
problem += int(skillName[59][1]) <= y[70]       # 地質学
problem += int(skillName[60][1]) <= y[71]       # 超会心
problem += int(skillName[61][1]) <= y[72]       # 挑戦者
problem += int(skillName[62][1]) <= y[73]       # 追跡の達人
problem += int(skillName[63][1]) <= y[74]       # 通常弾・通常矢強化
problem += int(skillName[64][1]) <= y[75]       # 釣り名人
problem += int(skillName[65][1]) <= y[76]       # 砥石使用高速化
problem += int(skillName[66][1]) <= y[77]       # 特殊射撃強化
problem += int(skillName[67][1]) <= y[78]       # 毒属性強化
problem += int(skillName[68][1]) <= y[79]       # 毒耐性
problem += int(skillName[69][1]) <= y[80]       # 毒ビン追加
problem += int(skillName[70][1]) <= y[81]       # 飛び込み
problem += int(skillName[71][1]) <= y[82]       # 泥耐性
problem += int(skillName[72][1]) <= y[83]       # 肉焼き名人
problem += int(skillName[73][1]) <= y[84]       # 熱ダメージ無効
problem += int(skillName[74][1]) <= y[85]       # 納刀術
problem += int(skillName[75][1]) <= y[86]       # 乗り名人
problem += int(skillName[76][1]) <= y[87]       # 破壊王
problem += int(skillName[77][1]) <= y[88]       # 剥ぎ取り鉄人
problem += int(skillName[78][1]) <= y[89]       # 爆破属性強化
problem += int(skillName[79][1]) <= y[90]       # 爆破ビン追加
problem += int(skillName[80][1]) <= y[91]       # 爆破やられ耐性
problem += int(skillName[81][1]) <= y[92]       # 抜刀術【技】
problem += int(skillName[82][1]) <= y[93]       # ハニーハンター
problem += int(skillName[83][1]) <= y[94]       # 早食い
problem += int(skillName[84][1]) <= y[95]       # 腹減り耐性
problem += int(skillName[85][1]) <= y[96]       # 飛燕
problem += int(skillName[86][1]) <= y[97]       # 火属性攻撃強化
problem += int(skillName[87][1]) <= y[98]       # 火耐性
problem += int(skillName[88][1]) <= y[99]       # ひるみ軽減
problem += int(skillName[89][1]) <= y[100]      # 風圧耐性
problem += int(skillName[90][1]) <= y[101]      # 笛吹き名人
problem += int(skillName[91][1]) <= y[102]      # 不屈
problem += int(skillName[92][1]) <= y[103]      # フルチャージ
problem += int(skillName[93][1]) <= y[104]      # 防御
problem += int(skillName[94][1]) <= y[105]      # 防御力ＤＯＷＮ耐性
problem += int(skillName[95][1]) <= y[106]      # 砲撃手
problem += int(skillName[96][1]) <= y[107]      # 砲術
problem += int(skillName[97][1]) <= y[108]      # 砲弾装填数ＵＰ
problem += int(skillName[98][1]) <= y[109]      # ボマー
problem += int(skillName[99][1]) <= y[110]      # 麻痺属性強化
problem += int(skillName[100][1]) <= y[111]     # 麻痺耐性
problem += int(skillName[101][1]) <= y[112]     # 麻痺ビン追加
problem += int(skillName[102][1]) <= y[113]     # 満足感
problem += int(skillName[103][1]) <= y[114]     # 見切り
problem += int(skillName[104][1]) <= y[115]     # 水属性攻撃強化
problem += int(skillName[105][1]) <= y[116]     # 水耐性
problem += int(skillName[106][1]) <= y[117]     # 水場・深雪適応
problem += int(skillName[107][1]) <= y[118]     # 耳栓
problem += int(skillName[108][1]) <= y[119]     # ランナー
problem += int(skillName[109][1]) <= y[120]     # 龍属性攻撃強化
problem += int(skillName[110][1]) <= y[121]     # 龍耐性
problem += int(skillName[111][1]) <= y[122]     # 龍封力強化
problem += int(skillName[112][1]) <= y[123]     # 裂傷耐性
problem += int(skillName[113][1]) <= y[124]     # 環境利用の知識
problem += int(skillName[114][1]) <= y[125]     # 蛮顎竜の力
problem += int(skillName[115][1]) <= y[126]     # 蛮顎竜の闘志
problem += int(skillName[116][1]) <= y[127]     # 蛮顎竜の覇気
problem += int(skillName[117][1]) <= y[128]     # 火竜の力
problem += int(skillName[118][1]) <= y[129]     # 火竜の奥義
problem += int(skillName[119][1]) <= y[130]     # 火竜の真髄
problem += int(skillName[120][1]) <= y[131]     # 桜火竜の奥義
problem += int(skillName[121][1]) <= y[132]     # 雌火竜の真髄
problem += int(skillName[122][1]) <= y[133]     # 熔山龍の奥義
problem += int(skillName[123][1]) <= y[134]     # 熔山龍の真髄
problem += int(skillName[124][1]) <= y[135]     # 風漂竜の恩恵
problem += int(skillName[125][1]) <= y[136]     # 風漂竜の恩寵
problem += int(skillName[126][1]) <= y[137]     # 風漂竜の覇気
problem += int(skillName[127][1]) <= y[138]     # 惨爪竜の力
problem += int(skillName[128][1]) <= y[139]     # 惨爪竜の奥義
problem += int(skillName[129][1]) <= y[140]     # 惨爪竜の真髄
problem += int(skillName[130][1]) <= y[141]     # 角竜の力
problem += int(skillName[131][1]) <= y[142]     # 角竜の奥義
problem += int(skillName[132][1]) <= y[143]     # 角竜の覇気
problem += int(skillName[133][1]) <= y[144]     # 爆鱗竜の守護
problem += int(skillName[134][1]) <= y[145]     # 爆鱗竜の覇気
problem += int(skillName[135][1]) <= y[146]     # 爆鎚竜の守護
problem += int(skillName[136][1]) <= y[147]     # 爆鎚竜の覇気
problem += int(skillName[137][1]) <= y[148]     # 滅尽龍の飢餓
problem += int(skillName[138][1]) <= y[149]     # 炎王龍の武技
problem += int(skillName[139][1]) <= y[150]     # 滅尽龍の覇気
problem += int(skillName[140][1]) <= y[151]     # 鋼龍の飛翔
problem += int(skillName[141][1]) <= y[152]     # 屍套龍の命脈
problem += int(skillName[142][1]) <= y[153]     # 屍套龍の霊脈
problem += int(skillName[143][1]) <= y[154]     # 幻獣の恩恵
problem += int(skillName[144][1]) <= y[155]     # 幻獣の恩寵
problem += int(skillName[145][1]) <= y[156]     # 幻獣の神秘
problem += int(skillName[146][1]) <= y[157]     # 冥灯龍の神秘
problem += int(skillName[147][1]) <= y[158]     # ギルドの導き
problem += int(skillName[148][1]) <= y[159]     # 調査団の導き
problem += int(skillName[149][1]) <= y[160]     # ガード強化
problem += int(skillName[150][1]) <= y[161]     # 心眼／弾導強化
problem += int(skillName[151][1]) <= y[162]     # 無属性強化
problem += int(skillName[152][1]) <= y[163]     # 弓溜め段階解放
problem += int(skillName[153][1]) <= y[164]     # 剛刃研磨
problem += int(skillName[154][1]) <= y[165]     # 炎妃龍の恩寵
problem += int(skillName[155][1]) <= y[166]     # 炎妃龍の真髄
problem += int(skillName[156][1]) <= y[167]     # アステラの祝福
problem += int(skillName[157][1]) <= y[168]     # 竜騎士の証
problem += int(skillName[158][1]) <= y[169]     # ウィッチャーの心得
problem += int(skillName[159][1]) <= y[170]     # 太古の神秘
problem += int(skillName[160][1]) <= y[171]     # 調査団の錬金術
problem += int(skillName[161][1]) <= y[172]     # 氷牙竜の秘技
problem += int(skillName[162][1]) <= y[173]     # 迅竜の真髄
problem += int(skillName[163][1]) <= y[174]     # 斬竜の真髄
problem += int(skillName[164][1]) <= y[175]     # 砕竜の真髄
problem += int(skillName[165][1]) <= y[176]     # 轟竜の真髄
problem += int(skillName[166][1]) <= y[177]     # 教官の導き
problem += int(skillName[167][1]) <= y[178]     # 恐暴竜の真髄
problem += int(skillName[168][1]) <= y[179]     # 雷狼竜の真髄
problem += int(skillName[169][1]) <= y[180]     # ギルドの見識
problem += int(skillName[170][1]) <= y[181]     # 冰龍の神秘
problem += int(skillName[171][1]) <= y[182]     # 溟龍の神秘
problem += int(skillName[172][1]) <= y[183]     # 地啼龍の神秘
problem += int(skillName[173][1]) <= y[184]     # 金火竜の真髄
problem += int(skillName[174][1]) <= y[185]     # 銀火竜の真髄
problem += int(skillName[175][1]) <= y[186]     # 金獅子の怒気
problem += int(skillName[176][1]) <= y[187]     # サバイバー
problem += int(skillName[177][1]) <= y[188]     # 動力源
problem += int(skillName[178][1]) <= y[189]     # 赤龍の封印
problem += int(skillName[179][1]) <= y[190]     # 万福の祝福
problem += int(skillName[180][1]) <= y[191]     # 大感謝の祝福
problem += int(skillName[181][1]) <= y[192]     # 満開の祝福
problem += int(skillName[182][1]) <= y[193]     # 情熱の祝福
problem += int(skillName[183][1]) <= y[194]     # ホラーナイトの祝福
problem += int(skillName[184][1]) <= y[195]     # 金獅子の闘志
problem += int(skillName[185][1]) <= y[196]     # 砕竜の闘志
problem += int(skillName[186][1]) <= y[197]     # 爛輝龍の真髄
problem += int(skillName[187][1]) <= y[198]     # 煌黒龍の神秘
problem += int(skillName[188][1]) <= y[199]     # 氷牙竜の絶技
problem += int(skillName[189][1]) <= y[200]     # 黒龍の伝説
problem += int(skillName[190][1]) <= y[201]     # New World
problem += int(skillName[191][1]) <= y[202]     # 災禍転福
problem += int(skillName[192][1]) <= y[203]     # 攻めの守勢
problem += int(skillName[193][1]) <= y[204]     # 鈍器使い
problem += int(skillName[194][1]) <= y[205]     # 業物／弾丸節約
problem += int(skillName[195][1]) <= y[206]     # クラッチ攻撃強化
problem += int(skillName[196][1]) <= y[207]     # 受け身術
problem += int(skillName[197][1]) <= y[208]     # 根性
problem += int(skillName[198][1]) <= y[209]     # 奮起
problem += int(skillName[199][1]) <= y[210]     # 陽動攻撃


status = problem.solve()

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
            print(str(skillName[i-11][0]) + 'Lv' + str(int(y[i].value())))
    print("\n")
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
    



