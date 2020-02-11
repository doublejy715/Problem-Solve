N = int(input())
data = list(map(int,input().split()))
result = [0]* N
for i in range(N):
    sum, pos = 0,0
    for j in range(i,N):
        if data[j] > pos:
            sum += data[j]
            pos = data[j]
        else:
            continue
    result[i] = sum

print(max(result))