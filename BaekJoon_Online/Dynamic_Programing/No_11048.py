import sys
N, M = map(int,sys.stdin.readline().split())
data = [[0 for _ in range(M+1)]]
data.extend(([0] + list(map(int,sys.stdin.readline().split()))) for _ in range(N))

for i in range(1,N+1):
    for j in range(1,M+1):
        data[i][j] += max(data[i-1][j],data[i-1][j-1],data[i][j-1])
print(data[N][M])