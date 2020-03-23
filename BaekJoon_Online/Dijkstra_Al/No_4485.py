import sys,heapq

Inf = sys.maxsize
dy,dx = (0,-1,0,1),(1,0,-1,0)
count = 0

def Dijkstra(maps,check,y,x):
    check[0][0] = maps[0][0]
    queue = []
    heapq.heappush(queue,[y,x,maps[y][x]])

    while queue:
        cur_y,cur_x,cur_money = heapq.heappop(queue)

        for i in range(4):
            ny, nx = cur_y+dy[i], cur_x+dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                # 여기다가 조건을 넣는다
                if check[ny][nx] > cur_money + maps[ny][nx]:
                    check[ny][nx] = cur_money + maps[ny][nx]
                    heapq.heappush(queue,[ny,nx,check[ny][nx]])
    return check[-1][-1]


def Input():
    global count
    N = int(input())
    if N == 0:
        sys.exit()
    else:
        maps = [list(map(int,input().split())) for _ in range(N)]
        check = [[Inf]*N for _ in range(N)]
        count += 1
    return N,maps,check

while True:
    N,maps,check = Input()

    result = Dijkstra(maps,check,0,0)
    print('Problem {}: {}'.format(count,result))