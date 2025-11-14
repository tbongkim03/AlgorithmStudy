word = input()
result = [-1 for _ in range(97, 123)]
for i in range(len(word)):
    idx = ord(word[i]) - 97
    if result[idx] == -1:
        result[idx] = i

for i in result:
    print(i, end=" ")