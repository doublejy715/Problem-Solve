import sys
sys.setrecursionlimit(100000)

def Area(N,maps,i,j,count,check):
    dy,dx = (0,-1,0,1),(1,0,-1,0)
    queue = []
    queue.append([i,j])
    while queue:
        point = queue.pop(0)
        check[point[0]][point[1]] = True
        for index in range(4):
            ny,nx = point[0] + dy[index], point[1] + dx[index]
            if 0 <= ny < N and 0 <= nx < N and not check[ny][nx] and maps[ny][nx] == maps[point[0]][point[1]]:
                queue.append([ny,nx])
    return count+1

def Input():
    N = int(input())
    maps_Ori = [list(input()) for _ in range(N)]
    maps_Col = [['0']*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maps_Ori[i][j] == 'G':
                maps_Col[i][j] = 'R'
            else:
                maps_Col[i][j] = maps_Ori[i][j]

    return N,maps_Ori,maps_Col


N,maps_Ori,maps_Col = Input()
check_O,check_C = [[False]*N for _ in range(N)], [[False]*N for _ in range(N)]
count_O, count_C = 0,0
for i in range(N):
    for j in range(N):
        if not check_O[i][j]:
            count_O = Area(N, maps_Ori,i,j,count_O,check_O)
        if not check_C[i][j]:
            count_C = Area(N, maps_Col, i, j, count_C, check_C)

print(count_O,count_C)