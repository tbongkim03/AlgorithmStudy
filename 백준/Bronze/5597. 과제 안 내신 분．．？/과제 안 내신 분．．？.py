students = [int(input()) for _ in range(28)]
students.sort()
for i in range(1,31):
    if not(i in students):
        print(i)
        