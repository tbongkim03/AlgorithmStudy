box, loop = map(int, input().split())
box_list = [i for i in range(1, box+1)]
for _ in range(loop):
    idx_a, idx_b = map(int, input().split())
    temp = box_list[idx_a - 1]
    box_list[idx_a - 1] = box_list[idx_b - 1]
    box_list[idx_b - 1] = temp
for i in box_list:
    print(i, end=" ")