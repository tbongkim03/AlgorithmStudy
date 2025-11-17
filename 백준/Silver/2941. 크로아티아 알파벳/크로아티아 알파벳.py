croatian = ["c=","c-","dz=","d-","lj","nj","s=","z="]
word = input()
for ca in croatian:
    word = word.replace(ca,"*")
print(len(word))
