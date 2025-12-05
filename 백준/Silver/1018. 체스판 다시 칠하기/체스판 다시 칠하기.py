n,m=map(int, input().split())
board=list([] for _ in range(n))
for i in range(n):
    board[i] = input()
# 입력받음 > start지점을 정하고 거기서 8x8 순회를 돌면서 몇개를 칠해야 하는지 구함.
starts=[]
for i in range(n):
    for j in range(m):
        try:
            if board[i][j] and board[i+7][j+7]:
                start=[i,j]
                starts.append(start)
        except:
            continue
# start 지점들을 전부 구했으니, 이제 그 곳부터 시작해서 몇 개 칠해야 완벽한 체스판이 되는지 구하기
cnt=64
cnts=[0 for _ in range(len(starts))]
for i in starts:
    x,y=map(int, i)
    # 시작이 B 인 경우
    if board[x][y] == "B":
        for j in range(8):
            for k in range(8):
                if j % 2 == 0 and k % 2 == 0: # B여야 할 위치
                    if board[x+j][y+k] != "B":
                        cnt-=1
                if j % 2 == 1 and k % 2 == 1: # B여야 할 위치
                    if board[x+j][y+k] != "B":
                        cnt-=1
                if j % 2 == 0 and k % 2 == 1: # W여야 할 위치
                    if board[x+j][y+k] != "W":
                        cnt-=1
                if j % 2 == 1 and k % 2 == 0: # W여야 할 위치
                    if board[x+j][y+k] != "W":
                        cnt-=1
    # 시작이 W 인 경우
    elif board[x][y] == "W":
        for j in range(8):
            for k in range(8):
                if j % 2 == 0 and k % 2 == 0: # W여야 할 위치
                    if board[x+j][y+k] != "W":
                        cnt-=1
                if j % 2 == 1 and k % 2 == 1: # W여야 할 위치
                    if board[x+j][y+k] != "W":
                        cnt-=1
                if j % 2 == 0 and k % 2 == 1: # B여야 할 위치
                    if board[x+j][y+k] != "B":
                        cnt-=1
                if j % 2 == 1 and k % 2 == 0: # B여야 할 위치
                    if board[x+j][y+k] != "B":
                        cnt-=1
    if cnt > 32:
        cnt=64-cnt
    cnts[starts.index(i)] = cnt
    cnt=64
print(min(cnts))