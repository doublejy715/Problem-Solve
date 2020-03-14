import copy
import sys
sys.setrecursionlimit(100000)

def Area(check_cp,i,j):
    dy,dx = (0,-1,0,1),(1,0,-1,0)
    for index in range(4):
        ny,nx = dy[index]+i,dx[index]+j
        if 0 <= ny < N and 0 <= nx < N and check_cp[ny][nx]:
            check_cp[ny][nx] = False
            Area(check_cp,ny,nx)

def Leak(i):
    for y in range(N):
        for x in range(N):
            if maps[y][x] <= i:
                check[y][x] = False


N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
check = [[True]*N for _ in range(N)]
result = 0
for i in range(0,101):
    Leak(i)
    count = 0
    check_cp = copy.deepcopy(check)
    for m in range(N):
        for n in range(N):
            if check_cp[m][n]:
                Area(check_cp,m,n)
                count += 1
    result = max(result,count)

print(result)