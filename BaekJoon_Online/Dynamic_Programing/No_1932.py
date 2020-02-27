N,data = int(input()),[]
for i in range(N):
    data.append(list(map(int,input().split())))

for i in range(1,N):
    for j in range(len(data[i])):
        if j == 0:
            data[i][j] += data[i-1][j]
        elif 0<j<len(data[i])-1:
            data[i][j] += max(data[i-1][j-1],data[i-1][j])
        else:
            data[i][j] += data[i-1][j-1]
print(max(data[len(data)-1]))