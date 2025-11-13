box, loop = map(int, input().split())
box_list = [0 for _ in range(box)]
for _ in range(loop):
    start, end, num = map(int, input().split())
    for i in range(start, end+1):
        box_list[i-1] = num
for i in box_list:
    print(i, end=" ")