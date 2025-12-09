n=int(input())
users=[]
for dt in range(n):
    age,name=input().split()
    users.append([int(age),name,dt])
users.sort(key=lambda x: (x[0],x[2]))
for i in users:
    print(i[0],i[1])