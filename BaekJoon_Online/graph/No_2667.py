def Bfs(maps,x,y):
    need_visit = []
    need_visit.append([y,x])
    dx,dy = (1,0,-1,0),(0,-1,0,1)
    count = 1

    while need_visit:
        ny,nx = need_visit.pop(0)
        maps[ny][nx] = 0

        for index in range(4):
            ty, tx = ny+dy[index], nx+dx[index]
            if 0 > ty or ty >= N or 0 > tx or tx >= N or [ty,tx] in need_visit :
                continue
            elif maps[ty][tx] == 1 :
                need_visit.append([ty,tx])
                count += 1
    return count

N = int(input())
maps = [list(map(int,input())) for _ in range(N)]
houses = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            counts = Bfs(maps,j,i)
            houses.append(counts)

print(len(houses),*(sorted(houses)),sep='\n')


"""
# 다른 재귀용법으로 만든 사람
def dfs(i, j, cnt):
    A[i][j] = 0 # 방문했음을 확인
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1] # 방향벡터
    for way in range(4):
        ii, jj = i + dx[way], j + dy[way]
        if ii>=0 and ii<N and jj>=0 and jj<N: # 범위체크
            if A[ii][jj] == 1: # 해당 부분이 1이면
                cnt = dfs(ii, jj, cnt+1)  # cnt 증가시켜서 근처 확인
    return cnt

N = int(input())
A= [list(map(int, list(input()))) for _ in range(N)]

li=[]
for i in range(N):
    for j in range(N):
        if A[i][j] == 1: # 그룹에 속한다면
            cnt = 0
            li.append(dfs(i, j,1))

print(len(li))
for ele in sorted(li):
    print(ele)
"""