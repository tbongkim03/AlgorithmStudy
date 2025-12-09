n=int(input())
xys=[]
for i in range(n):
    x, y = map(int, input().split())
    xys.append([x,y])
xys.sort()
for i in xys:
    print(*i)