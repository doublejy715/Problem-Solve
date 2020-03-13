import sys
sys.setrecursionlimit(100000)
read = sys.stdin.readline
def Clean(maps,r,c,d,count):
    maps[r][c] = 2
    dx,dy = (-1,0,1,0),(0,-1,0,1)

    # 2.c(뒤를 제외한 방향이 벽 or 청소한 경우
    if maps[r+dy[(d-1)%4]][c+dx[(d-1)%4]] > 0 and maps[r+dy[(d-3)%4]][c+dx[(d-3)%4]] > 0 and maps[r+dy[(d-4)%4]][c+dx[(d-4)%4]] > 0 and maps[r+dy[(d-2)%4]][c+dx[(d-2)%4]] > 0:
        # 2.c.1 뒤가 벽이 아닌경우
        if maps[r+dy[(d-1)%4]][c+dx[(d-1)%4]] == 2:
            return Clean(maps,r+dy[(d-1)%4],c+dx[(d-1)%4],d,count)

        # 2.c.1 뒤가 벽인 경우
        elif maps[r+dy[(d-1)%4]][c+dx[(d-1)%4]] == 1:
            return count


    # 2.a
    elif maps[r + dy[d]][c + dx[d]] == 0:
        return Clean(maps, r + dy[d], c + dx[d], (d - 1) % 4, count + 1)
    # 2.b
    elif maps[r + dy[d]][c + dx[d]] > 0:
        return Clean(maps, r, c, (d - 1) % 4, count)

N, M = map(int,read().split())
r,c,d = map(int,read().split())
maps = [list(map(int,read().strip().split())) for _ in range(N)]
print(Clean(maps,r,c,d,1))
