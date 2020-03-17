def Round(i,j):
    global count
    maps[i][j] = 1
    dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)
    for index in range(4):
        ny, nx = dy[index]+i, dx[index]+j
        if 0<= nx < N and 0<= ny < M and maps[ny][nx] == 0:
            count += 1
            Round(ny,nx)

def Check():
    global count
    for i in range(M+1):
        for j in range(N+1):
            if maps[i][j] == 0:
                count = 0
                Round(i,j)
                result.append(count)


def Block(x1,y1,x2,y2):
    for i in range(y1,y2+1):
        for j in range(x1,x2+1):
            maps[i][j] = 1


M,N,K = map(int,input().split())
maps = [list(0 for _ in range(N+1)) for _ in range(M+1)]
result = []
count = 0
for i in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    Block(x1,y1,x2,y2)
Check()
print(result)