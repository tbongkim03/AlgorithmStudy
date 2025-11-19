n, m = map(int, input().split())
matrix_A = []
matrix_B = []
matrix_C = [[0 for _ in range(m)] for _ in range(n)]
for i in range(2*n):
    if i < n:
        matrix_A.append(list(map(int, input().split())))
    else:
        matrix_B.append(list(map(int, input().split())))
for vy in range(n):
    for vx in range(m):
        matrix_C[vy][vx] = matrix_A[vy][vx] + matrix_B[vy][vx]
for p in matrix_C:
    print(*p)