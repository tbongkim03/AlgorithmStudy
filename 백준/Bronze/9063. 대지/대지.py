n = int(input())
xs = []
ys = []
for _ in range(n):
    a,b=map(int, input().split())
    xs.append(a)
    ys.append(b)
print((max(xs) - min(xs)) * (max(ys) - min(ys)))