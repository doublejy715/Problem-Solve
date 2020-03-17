import sys
sys.setrecursionlimit(100000)

def Spread(i,j,k,Days):
    maps[i][j][k] = 2             # 퍼진 구역은 다르게 표시
    dz,dy,dx = (0,0,0,0,1,-1),(0,1,0,-1,0,0),(1,0,-1,0,0,0)
    for index in range(6):
        nz,ny,nx = i+dz[index],j+dy[index],k+dx[index]
        if 0 <= nz < L and 0 <= ny < N and 0 <= nx < M and maps[nz][ny][nx] <= 1: # 어떻게 한번에 모두 2로 바꿀 수 있을까?
            maps[nz][ny][nx] = 2 # 상하좌우앞뒤 다 바꿔준다.
            Spread(nz,ny,nx,Days+1) # 6번의 호출로 대신한다.???

def Check_First():
    count_0 = 0
    for i in range(L):
        for j in range(N):
            for k in range(M):
                if maps[i][j][k] == 0:
                    count_0 += 1
    if count_0 == 0:
        print(0)
        sys.exit()

def Check_Second(Days):
    for i in range(L):
        for j in range(N):
            for k in range(M):
                if maps[i][j][k] == 0:
                    print(-1)
                    sys.exit()
    print(Days)


M, N, L = map(int,input().split())
maps = [[list(map(int,input().split())) for _ in range(N)] for _ in range(L)]
Check_First()
Days = 0
for i in range(L):
    for j in range(N):
        for k in range(M):
            if maps[i][j][k] == 1:
                Spread(i,j,k,Days)


Check_Second(Days)