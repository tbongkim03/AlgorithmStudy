nums=list(map(int, input().split()))
m = nums.index(max(nums))
while True:
    if nums[m] >= sum(nums) - nums[m]:
        nums[m]-=1
    else:
        print(sum(nums))
        break