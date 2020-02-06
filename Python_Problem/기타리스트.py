n,s,m = map(int,input().split(' '))
list1 = list(map(int,input().split(' ')))
data = [[0]*(m+1) for i in range(n+1)]

data[0][s] = 1

for i in range(1,n+1):
    for j in range(m+1):
        if data[i-1][j] == 0:
            continue
        if j - list1[i -1] >= 0:
            data[i][j-list1[i-1]] = 1
        if j + list1[i-1] <= m:
            data[i][j + list1[i-1]] = 1

result = -1
for i in range(m,-1,-1):
    if data[n][i] == 1:
        result = i
        break
print(result)