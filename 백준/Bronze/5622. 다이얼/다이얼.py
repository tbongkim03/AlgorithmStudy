word = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
sec = 0
for i in word:
    for j in dial:
        if i in j:
            sec += dial.index(j) + 3
         
print(sec)