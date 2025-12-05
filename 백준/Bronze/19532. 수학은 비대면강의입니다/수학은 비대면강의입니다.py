a,b,c,d,e,f=map(int, input().split())
# a*x + b*y = c
# d*x + e*y = f
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i + b*j == c) and (d*i + e*j == f):
            result=[i,j]
            break
print(*result)