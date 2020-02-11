import sys
sys.setrecursionlimit(100000)
def dfs(x,y):
    visited[x][y] = True
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx,dy in directions:
        if x+dx<0 or x+dx >= n or y+dy < 0 or y+dy > m: # 구역의 범위부터 지정해 주고
            continue
        if array[x+dx][y+dy] and not visited[x+dx][y+dy]: # 해당 조건을 말해준다.
            dfs(x+dx,y+dy)



for _ in range(int(input())):
    m,n,k = map(int,input().split())
    array = [[0]*m for _ in range(n)] # 2차원 배열을 지정할 때는 이렇게 한다.
    visited = [[False]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int,input().split())
        array[x][y] = 1
    result = 0

    for i in range(n):
        for j in range(m):
            if array[i][j] and not visited[i][j]: # array에서 1이고, visited[i][j]가 True가 아니라면, False
                dfs(i,j)
                result += 1
    print(result)