score = [sum(map(int,input().split())) for _ in range(5)]
for i in range(len(score)):
    if max(score) == score[i]:
        print(i+1, score[i])