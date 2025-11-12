start_h, start_m = map(int, input().split())
cooking_minuate = int(input())
if start_m + cooking_minuate > 59:
    start_h += ((start_m + cooking_minuate) // 60)
    start_m = (start_m + cooking_minuate) % 60
else:
    start_m += cooking_minuate
if start_h > 23:
    start_h %= 24
print(start_h, start_m)