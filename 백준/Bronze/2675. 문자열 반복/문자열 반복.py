loop = int(input())
for _ in range(loop):
    cnt, word = input().split()
    for char in word:
        print(char * int(cnt), end="")
    print()