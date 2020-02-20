import sys

test_case = int(sys.stdin.readline())
dx,dy = [1,0,-1,0],[0,1,0,-1]

def Bfs(x,y):
    check[x][y] = 1
    for i in range(4):
        XX, YY = x+dx[i], y+dy[i]
        if check[XX][YY] or not B[XX][YY]:
            continue
        Bfs(XX,YY)

for _ in range(test_case):
    # 변수 작성
    m, n, k = map(int,sys.stdin.readline().split())
    B = [[0 for index1 in range(m+2)] for index2 in range(n+2)]
    check = [[0 for index1 in range(m+2)] for index2 in range(n+2)]

    # input() 받기
    for i in range(k):
        x, y = map(int,sys.stdin.readline().split())
        B[y+1][x+1] = 1

    result = 0
    for x in range(1,n+1):
        for y in range(1,m+1):
            if check[x][y] or not B[x][y]:
                continue
            Bfs(x,y)
            result += 1

    print(result)
