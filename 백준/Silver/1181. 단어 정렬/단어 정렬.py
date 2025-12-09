#길이가 짧은 것부터
#길이가 같으면 사전 순으로
n=int(input())
words=[]
for i in range(n):
    words.append(input())
words=list(set(words))
words.sort(key=lambda x: (len(x),x))
print(*words, sep="\n")