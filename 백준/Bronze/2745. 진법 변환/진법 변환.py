N, B = input().split()
B = int(B)
total = 0

N=N[::-1]
for i in range(len(N)):
    ch = N[i]
    if '0' <= ch <= '9':
        val = int(ch)
    else:
        val = ord(ch) - ord('A') + 10
    total += val * (B ** i)
print(total)