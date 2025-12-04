n=int(input())
result=0
for i in range(1, n):
    nums=list(map(int, str(i)))
    m = sum(nums) + i
    if m == n:
        result=i
        break
print(result)