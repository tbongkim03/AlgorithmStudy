ranks = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
score_sum = 0
scorexmean_sum = 0
while True:
    try:
        _, score, rank = input().split()
        if rank != "P":
            score_sum += float(score)
            scorexmean_sum += float(score) * ranks[rank]
    except:
        break
print(scorexmean_sum / score_sum)