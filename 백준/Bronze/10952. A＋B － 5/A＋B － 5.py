a, b = map(int, input().split())
print(a+b)
while(True):
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(a+b)