n = int(input())
nums = list(map(int, input().split()))
check = 0
cnt = 0
for i in range(n):
    for j in range(1, nums[i]):
        # 나눠떨어지는 수가 있으면 체크를 증가시킴.
        # 체크가 1이면 소수임
        if nums[i] % j == 0:
            check += 1
    if check == 1:
        cnt += 1
    check = 0
print(cnt)