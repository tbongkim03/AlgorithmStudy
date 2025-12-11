import sys
input=sys.stdin.readline
n=int(input())
logdic={}
for i in range(n):
    k,v=input().split()
    logdic[k]=v
    if v=="leave":
        logdic.pop(k)
loglist=list(k for k in logdic)
loglist.sort(reverse=True)
print("\n".join(map(str, loglist)))