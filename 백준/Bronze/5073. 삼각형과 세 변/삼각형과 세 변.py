a,b,c=map(int, input().split())
while not(a==b==c==0):
    temp = [a,b,c]
    if max(temp) >= sum(temp) - max(temp):
        print("Invalid")
    elif len(set(temp)) == 1:
        print("Equilateral")
    elif len(set(temp)) == 2:
        print("Isosceles")
    elif len(set(temp)) == 3:
        print("Scalene")
    a,b,c=map(int, input().split())