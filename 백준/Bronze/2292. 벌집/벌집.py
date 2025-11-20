n = int(input())
i = 0
limit = 1
before_limit = 1
while True:
    limit += 6*i
    i+=1
    if before_limit <= n <= limit:
        break
    else:
        before_limit = limit
print(i)