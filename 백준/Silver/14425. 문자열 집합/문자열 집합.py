import sys
input=sys.stdin.readline
n,m=map(int, input().split())
words=set(input() for _ in range(n))
targets=list(input() for _ in range(m))
cnt=0
for i in targets:
    if i in words:
        cnt+=1
print(cnt)