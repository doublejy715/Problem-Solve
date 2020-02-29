import sys
sys.setrecursionlimit(100000)
dx,dy = (0,1,1,1,0,-1,-1,-1),(1,1,0,-1,-1,-1,0,1)
def Bfs(i,j,Maps):
    Maps[i][j] = 0
    for h in range(8):
        if 0 > i + dy[h] or i + dy[h] >= len(Maps) or 0 > j + dx[h] or j + dx[h] >= len(Maps[0]):
            continue
        elif Maps[i+dy[h]][j+dx[h]] == 1:
            Bfs(i+dy[h],j+dx[h],Maps)

def Input():
    w, h = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(h)]
    return w,h,maps

while True:
    count = 0
    W,H,Maps = Input()
    if not W and not H :
        sys.exit()
    for i in range(H):
        for j in range(W):
            if Maps[i][j] == 1:
                Bfs(i,j,Maps)
                count += 1
    print(count)
