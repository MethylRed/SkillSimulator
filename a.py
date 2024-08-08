weapon = [[3,3,3,3]]

slot = [0,0,0]
for i in range(4):
    for j in range(int(weapon[0][i])):
        slot[j] += 1
print("slot:" + str(slot))