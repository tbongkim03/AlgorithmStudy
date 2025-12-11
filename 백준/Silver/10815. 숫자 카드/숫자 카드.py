import sys
input=sys.stdin.readline
n=int(input())
deck=set(map(int, input().split()))
m=int(input())
needs=list(map(int, input().split()))
result=[0]*m
for i in range(len(needs)):
    if needs[i] in deck:
        result[i] = 1
print(" ".join(map(str, result)))