n=int(input())
xys=[]
for i in range(n):
    x,y=map(int, input().split())
    xys.append([y,x])
xys.sort()
for i in xys:
    print(i[1],i[0])