count, target = map(int, input().split())
nums = [ 0 for _ in range(count)]
nums = list(map(int, input().split()))
for i in nums:
    if i < target:
        print(i, end = " ")