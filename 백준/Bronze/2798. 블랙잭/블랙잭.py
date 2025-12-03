n, m = map(int, input().split())
deck = list(map(int, input().split()))
dif = 999999999
result = 0
for i in range(len(deck)):
    for j in range(i+1, len(deck)):
        for k in range(j+1, len(deck)):
            total = deck[i] + deck[j] + deck[k]
            if total <= m and 0 <= m - total <= dif:
                dif = m - total
                result = total
print(result)