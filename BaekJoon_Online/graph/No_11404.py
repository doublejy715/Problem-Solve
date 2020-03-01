import sys
Inf = sys.maxsize
N, edges = int(input()), int(input())
graph = [[Inf for _ in range(N)] for _ in range(N)]
for _ in range(edges):
    a,b,edge = map(int,input().split())

    graph[a-1][b-1] = min(graph[a-1][b-1],edge)

for l in range(len(graph)):
    graph[l][l] = 0

# i : 한번 거치는 노드, j : 출발노드, k : 목표노드
for i in range(len(graph)):
    for j in range(len(graph)):
        for k in range(len(graph)):
            graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])

for i in range(N):
    for j in range(N):
        if graph[i][j] == Inf:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()