##def cub(x,y):
##    return x+y
###c = filter(cub,range(1,11))
###c = map(cub, range(2,25))
##print reduce(cub,range(1, 25))

matrix = [[1, 2, 7, 5], [5, 7, 3, 7], [6, 4, 8, 9]]
a = []
print matrix[0]
for i in range(4):
    a.append([row[i] for row in matrix])

print a
