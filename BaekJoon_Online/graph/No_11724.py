def Set(maps):
    for i in range(1, N + 1):
        parent[i] = i
        rank[i] = 0

    for i in range(M):
        x, y = map(int, input().split())
        maps.append([min(x, y), max(x, y)])
    maps.sort()
    return maps

def Output():
    result = set()
    for i in range(N):
        result.add(parent[i + 1])
    print(len(result))

def Find(x):
    if parent[x] != x:
        parent[x] = Find(parent[x])
    return parent[x]

def Union(x,y):
    parent_x, parent_y = Find(x), Find(y)

    if rank[parent_x] > rank[parent_y]:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y
        if rank[parent_x] == rank[parent_y]:
            rank[parent_y] += 1

N, M = map(int,input().split())
parent,rank,maps = dict(), dict(), []

maps = Set(maps)
for x,y in maps:
    Union(x,y)
Output()

