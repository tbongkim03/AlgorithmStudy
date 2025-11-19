matrix = [list(map(int, input().split())) for _ in range(9)]
maxV = -999
maxy = 0
maxx = 0
for y in range(9):
    for x in range(9):
        if matrix[y][x] > maxV:
            maxV = matrix[y][x]
            maxy = y + 1
            maxx = x + 1
print(maxV)
print(maxy, maxx)