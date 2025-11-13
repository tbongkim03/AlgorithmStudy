cnt = int(input())
nums = [ 0 for _ in range(cnt) ]
nums = list(map(int, input().split()))
target = int(input())
result = 0
for i in nums:
    if target == i:
        result += 1
print(result)