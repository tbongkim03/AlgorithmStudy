import sys
input=sys.stdin.readline
n=int(input())
nums=list(map(int, input().split()))
snums=sorted(list(set(nums)))
sorts={v:i for i, v in enumerate(snums)}
for i in nums:
    print(sorts[i], end=" ")