import sys
from collections import Counter
input=sys.stdin.readline

n=int(input())
nums=list(map(int, input().split()))

m=int(input())
doyouhave=list(map(int, input().split()))

counter = Counter(nums)

print(" ".join(str(counter[x]) for x in doyouhave))