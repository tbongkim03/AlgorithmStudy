xs=[]
ys=[]
for _ in range(3):
    resultx = 0
    resulty = 0
    x,y=map(int, input().split())
    xs.append(x)
    ys.append(y)
    for i in xs:
        resultx ^= i
    for j in ys:
        resulty ^= j
print(resultx, resulty)