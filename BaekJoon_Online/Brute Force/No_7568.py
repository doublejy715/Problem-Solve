N = int(input())
data= []
for i in range(N):
    data.append(list(map(int,input().split())))

for i in range(N):
    count = 0
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    print(count+1, end=' ')