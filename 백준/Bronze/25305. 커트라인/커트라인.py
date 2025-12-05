people,cut=map(int, input().split())
scores=list(map(int, input().split()))
scores.sort(reverse=True)
cutline=scores[cut-1]
print(cutline)