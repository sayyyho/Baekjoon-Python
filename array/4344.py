N = int(input())
count = 0
score_mean = 0

for i in range(N):
    score = list(map(int, input().split()))
    score_mean = (sum(score) - score[0]) / score[0]
    for k in range(score[0]):
        if (score[k+1] > score_mean):
            count += 1
    print("%0.3f%%" % (100* count / score[0]))
    count = 0