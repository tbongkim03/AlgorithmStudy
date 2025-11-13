subjects = int(input())
scores = [0 for _ in range(subjects)]
scores = list(map(int, input().split()))
m = max(scores)
for i in range(subjects):
    #if scores[i] != m: 아니 최대값에 맞춰서 점수를 바꾼다면서 최대값도 바꿔서 100점으로 계산하는거였네
    scores[i] = scores[i]/m*100
print(sum(scores)/subjects)