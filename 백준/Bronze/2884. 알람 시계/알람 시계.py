# 입력된 시각의 45분 전 시각 구하기
H, M = map(int, input().split())
if M < 45:
    if H > 0:
        H -= 1
    else:
        H = 23
    M = 60 + (M - 45)
else:
    M -= 45
print(H, M)