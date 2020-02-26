N = int(input())
data = []
score = [ 0 for _ in range(N)]
for i in range(N):
    data.append(tuple(map(int,input().split())))
for i in range(3):
    for index1 in range(N):
        check = False
        for index2 in range(N):
            if index1 == index2:
                continue
            elif data[index1][i] == data[index2][i]:
                check = True
                break
        if not check:
            score[index1] += data[index1][i]
print(*score,sep='\n')