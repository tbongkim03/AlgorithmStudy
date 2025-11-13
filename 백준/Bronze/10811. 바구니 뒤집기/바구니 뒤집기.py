box, loop = map(int, input().split())
box_list = [i for i in range(1, box+1)]
for _ in range(loop):
    start, end = map(int, input().split())
    box_list[start-1:end] = box_list[start-1:end][::-1]
for i in box_list:
    print(i, end=" ")