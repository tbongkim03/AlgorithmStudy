word = input().upper()
alphabet = [0 for _ in range(ord('A'), ord('Z')+1)]
cnt = 0
for char in word:
    index = ord(char) - ord('A')
    alphabet[index] += 1

for i in alphabet:
    if i == max(alphabet):
        cnt += 1
if cnt > 1:
    print("?")
else:
    print(chr(alphabet.index(max(alphabet))+ord('A')))