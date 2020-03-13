import copy

def Check(maps):
    count = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0 :
                count += 1
    return count

def Spread(maps,spot2,y_2,x_2):
    maps[y_2][x_2] = 2
    dy,dx = (0,-1,0,1),(1,0,-1,0)
    for index in range(4):
        ny,nx = y_2+dy[index],x_2+dx[index]
        if 0 <= ny < N and 0 <= nx < M and maps[ny][nx] == 0:
            Spread(maps,spot2,ny,nx)


def Wall(maps1,spot0,counts):
    for i in range(len(spot0)):
        for j in range(i+1,len(spot0)):
            for k in range(j+1,len(spot0)):
                maps = copy.deepcopy(maps1)
                y1,x1 = spot0[i]
                y2,x2 = spot0[j]
                y3,x3 = spot0[k]
                maps[y1][x1], maps[y2][x2], maps[y3][x3] = 1,1,1
                for y_2,x_2 in spot2:
                    Spread(maps,spot2,y_2,x_2)

                counts = max(counts,Check(maps))
    return counts

N,M = map(int,input().split())
maps, spot0, spot2 = [],[], []
counts = 0
for i in range(N):
    line = list(map(int,input().split()))
    maps.append(line)
    for j in range(M):
        if line[j] == 0:
            spot0.append([i,j])
        if line[j] == 2:
            spot2.append([i,j])

print(Wall(maps,spot0,counts))
