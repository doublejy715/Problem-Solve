N = int(input())
data = [[0 for _ in range(N+1)] for i in range(N+1)]

for i in range(N):
    for j in range(i):
        data[i][j] = input()

print(data)