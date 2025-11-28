n = int(input())
loop = n + 1
i = 2
if n != 1:
    while True:
        if n % i == 0:
            n //= i
            print(i)
        else:
            i += 1
        if n < i:
            break