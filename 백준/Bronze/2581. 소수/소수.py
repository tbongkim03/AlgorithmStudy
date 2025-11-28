m=int(input())
n=int(input())
nums = []
check = 0
for i in range(m, n+1):
    for j in range(1, i):
        if i % j == 0:
            check += 1
    if check == 1:
        nums.append(i)
    check = 0
if len(nums) == 0:
    print(-1)
else:
    print(sum(nums))
    print(nums[0])