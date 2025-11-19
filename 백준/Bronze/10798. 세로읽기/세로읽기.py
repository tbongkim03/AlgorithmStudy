matrix = [list(input()) for _ in range(5)]
maxlen = -999
for y in matrix:
    if len(y) > maxlen:
        maxlen = len(y)
        
for i in range(maxlen):
    for j in range(len(matrix)):
        try:
            if matrix[j][i]:
                print(matrix[j][i], end="")
        except:
            continue