white = list(map(int, input().split()))
black = [1,1,2,2,2,8]
result = [0,0,0,0,0,0]
for unit in range(len(black)):
    result[unit] = black[unit] - white[unit]
    
print(*result)