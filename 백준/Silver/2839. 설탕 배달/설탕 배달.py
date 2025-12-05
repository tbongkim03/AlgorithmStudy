n=int(input())
x=9999
y=9999
for i in range(5000):
    for j in range(5000):
        if 5*i+3*j == n:
            if i+j<=x+y:
                x,y=i,j
if x!=9999 and y!=9999:
    print(x+y)
else:
    print(-1)