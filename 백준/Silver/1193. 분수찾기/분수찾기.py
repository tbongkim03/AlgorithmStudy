n=int(input())
line = 1
while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    a=1 + (n-1)
    b=line - (n-1)
elif line % 2 == 1:
    a=line - (n-1)
    b=1 + (n-1)
print(f"{a}/{b}")