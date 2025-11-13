total_amount = int(input())
total_things = int(input())
for _ in range(total_things):
    price, count = map(int, input().split())
    total_amount -= (price * count)

if total_amount == 0:
    print("Yes")
else:
    print("No")