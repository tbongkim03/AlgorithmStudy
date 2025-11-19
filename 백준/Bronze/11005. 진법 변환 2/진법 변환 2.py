num, B = map(int, input().split())
result = []
while True:
    mok = num // B
    qx = num % B
    num = mok
    result.append(qx)
    if mok == 0:
        break
for i in range(len(result)):
    if result[i] > 9:
        result[i] = chr(result[i] + ord('A') - 10)
for j in reversed(result):
    print(j, end="")