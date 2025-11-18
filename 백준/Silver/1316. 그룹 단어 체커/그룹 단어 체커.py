loop = group_word = int(input())
for _ in range(loop):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+2:]:
            group_word -= 1
            break
print(group_word)