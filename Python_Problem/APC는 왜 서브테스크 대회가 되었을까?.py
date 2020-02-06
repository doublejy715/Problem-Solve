N,L,K = map(int,input().split(' '))
data = list()
for index in range(N):
    datas = list(map(int,input().split(' ')))
    data.append(datas)

score = 0
count = []
for index1 in range(len(data)):
    if data[index1][1] <= L and K > 0 :
        count.append(index1)
        score += 140
        K -= 1

for index2 in range(len(data)):
    if K > 0 and data[index2][0] <= L:
        if index2 not in count:
            count.append(index2)
            score += 100
            K -= 1

print(score)