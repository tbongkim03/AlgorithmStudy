count = int(input())
nums = [0 for _ in range(count)]
nums = list(map(int, input().split()))
print(min(nums), max(nums))