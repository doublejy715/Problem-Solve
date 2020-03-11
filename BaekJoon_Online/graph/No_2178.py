def Bfs(maps,x,y):
    need_visit, visited = [], []
    need_visit.append([y,x])
    check = [[0 for _ in range(M)] for _ in range(N)]
    check[0][0] = 1
    dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)

    while need_visit:
        node_y,node_x = need_visit.pop(0)
        visited.append([node_y,node_x])

        for i in range(4):
            if 0 <= node_y+dy[i] < N and 0<= node_x+dx[i] < M and maps[node_y+dy[i]][node_x+dx[i]] == 1 and [node_y+dy[i],node_x+dx[i]] not in visited and [node_y+dy[i],node_x+dx[i]] not in need_visit:
                need_visit.append([node_y+dy[i],node_x+dx[i]])
                check[node_y+dy[i]][node_x+dx[i]] = check[node_y][node_x] + 1

    return check[N-1][M-1]

N,M = map(int,input().split())
maps = [list(map(int,input())) for _ in range(N)]
# 너비가 더 수월하다 막다른곳에 들어가거나 목표지점에 들어가면, 기록해 주면 된다. DFS하면 끝까지 들어간 뒤 돌아오기 때문에 시간이 더 오래 걸릴 수 있다.
print(Bfs(maps,0,0))

"""
# 매우 빠른 코드(why?)
from _collections import deque
import sys

def search(i, j, cnt):
    global N, M
    for k in range(4):
        if 0 <= i+di[k] < N and 0 <= j+dj[k] < M:
            if maze[i+di[k]][j+dj[k]] == 1 and visited[i+di[k]][j+dj[k]] == 0:
                visited[i + di[k]][j + dj[k]] = 1
                que.append([i+di[k], j+dj[k], cnt+1])

que = deque()
di = [1,-1,0,0]
dj = [0,0,1,-1]

input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, list(input())[:-1])))
que.append([0,0,1])
visited = [[0]*M for _ in range(N)]
while que:
    i, j, cnt = que.popleft()
    if i == N - 1 and j == M - 1:
        result = cnt
        break
    search(i, j, cnt)
print(result)
"""