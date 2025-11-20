T = int(input())
result = []
for _ in range(T):
    change = int(input())
    result = []
    result.append(change // 25)
    result.append(change % 25 // 10)
    result.append(change % 25 % 10 // 5)
    result.append(change % 25 % 10 % 5 // 1)
    print(*result)
    