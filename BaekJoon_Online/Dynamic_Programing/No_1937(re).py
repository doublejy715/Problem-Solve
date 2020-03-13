import sys
read = sys.stdin.readline
sys.setrecursionlimit(300000)


def Start(i,j,count):
    global result
    dy,dx = (0,-1,0,1),(1,0,-1,0)
    for index in range(4):
        ny, nx = i+dy[index], j+dx[index]
        if 0 <= ny < N and 0 <= nx < N and maps[ny][nx] > maps[i][j]:
            result = max(result,count)
            Start(ny,nx,count+1)

N = int(read())
maps = [ list(map(int,read().strip().split())) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        Start(i,j,1)
print(result+1)
