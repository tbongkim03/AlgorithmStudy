n = int(input())
nums = []
while n!=-1:
    for i in range(1, n):
        if n % i == 0:
            nums.append(i)
    if sum(nums) == n:
        print(n, "= ", end="")
        print(*nums, sep=" + ")

    if sum(nums) != n:
        print(f"{n} is NOT perfect.")
    n = int(input())
    nums = []