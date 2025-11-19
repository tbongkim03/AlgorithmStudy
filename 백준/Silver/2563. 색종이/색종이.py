cnt = int(input())
s = set()
for _ in range(cnt):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            s.add((i,j))
print(len(s))