matrix = [[1, 4, 7,11],
          [2, 5, 8,12],
          [3, 6, 9,13],
          [4, 7, 10,14]]
trans = []
for i in range(4):
    temp = [row[i] for row in matrix]
    trans.append(temp)
print trans
