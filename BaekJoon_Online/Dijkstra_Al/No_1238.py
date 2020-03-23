import sys
import heapq
read = sys.stdin.readline

def Dijkstra(graph,start):
    distance = {index : float('inf') for index in range(1,len(graph))}
    distance[start] = 0
    queue = []
    heapq.heappush(queue,[distance[start],start])

    while queue:
        cur_dis,cur_node = heapq.heappop(queue)

        if distance[cur_node] < cur_dis:
            continue

        for next_node,next_dis in graph[cur_node]:
            if (distance[cur_node]+next_dis) < distance[next_node]:
                distance[next_node] = distance[cur_node]+next_dis
                heapq.heappush(queue,[distance[next_node],next_node])

    return distance


def Input():
    N,M,X = map(int,read().strip().split())
    mygraph1, mygraph2 = [[] for _ in range(N+1)], [[] for _ in range(N+1)]
    for i in range(M):
        start, end, edge = map(int,read().strip().split())
        mygraph1[start].append([end,edge])
        mygraph2[end].append([start,edge])

    return N,M,X,mygraph1,mygraph2

N,M,X,mygraph1,mygraph2 = Input()
go_distance = Dijkstra(mygraph1,X)
back_distance = Dijkstra(mygraph2,X)

for i in range(1,len(go_distance)+1) :
    go_distance[i] += back_distance[i]
print(max(go_distance.values()))
