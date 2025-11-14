loop = int(input())
words = [input() for _ in range(loop)]
for word in words:
    print(f"{word[0]}{word[-1]}")