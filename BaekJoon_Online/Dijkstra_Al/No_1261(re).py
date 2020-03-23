import sys
sys.setrecursionlimit(100000)
Inf = sys.maxsize

def Dijkstra(maps,result,now_y,now_x):
    dy,dx = (0,-1,0,1),(1,0,-1,0)

    if [now_y,now_x] == [y-1,x-1]:
        return

    for index in range(4):
        next_y, next_x = now_y + dy[index], now_x + dx[index]
        if 0 <= next_y < y and 0 <= next_x < x and maps[next_y][next_x]:
            if result[now_y][now_x] + 1 < result[next_y][next_x]:
                result[next_y][next_x] = result[now_y][now_x] + 1
                Dijkstra(maps,result,next_y,next_x)



def Input():
    y,x = map(int,input().strip().split())
    maps = [list(map(int,input())) for _ in range(y)]

    return maps,y,x

maps,y,x = Input()
result = [[Inf]*x for _ in range(y)]
result[0][0] = 0
Dijkstra(maps,result,0,0)
print(result[y-1][x-1])

"""
# 이게 맞는것
import sys
from collections import deque
 
n, m = map(int, sys.stdin.readline().split())
a = []
 
for i in range(m):
    a.append(sys.stdin.readline())
 
dist = [[-1]*n for _ in range(m)]
dist[0][0] = 0
q = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q.append([0, 0])
 
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx>=0 and nx<m and ny >=0 and ny<n:
            if dist[nx][ny] == -1:
                if a[nx][ny] == '0':
                    q.appendleft([nx, ny])
                    dist[nx][ny] = dist[x][y]
                elif a[nx][ny] == '1':
                    q.append([nx, ny])
                    dist[nx][ny] = dist[x][y]+1
 
print(dist[m-1][n-1])

"""