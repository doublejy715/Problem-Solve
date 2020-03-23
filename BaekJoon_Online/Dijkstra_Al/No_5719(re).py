# 간선을 어떻게 지우지...
import sys,heapq

Inf = sys.maxsize
input = sys.stdin.readline

def Dijkstra(mygraph,start):
    distance = [Inf]*N
    distance[start] = 0
    queue,result = [],set()
    heapq.heappush(queue,[distance[start],start])

    while queue:
        cur_dis,cur_sp = heapq.heappop(queue)

        if cur_dis > distance[cur_sp]:
            continue

        for next_sp,next_dis in mygraph[cur_sp]:
            if next_sp == end:
                result.add(distance[cur_sp]+next_dis)
            if (distance[cur_sp]+next_dis) < distance[next_sp]:
                distance[next_sp] = distance[cur_sp]+next_dis
                heapq.heappush(queue,[distance[next_sp],next_sp])
    return result



def Input():
    N,M = map(int,input().split())
    if N == M == 0:
        sys.exit()
    start, end = map(int,input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        x,y,edge = map(int,input().strip().split())
        graph[x].append([y,edge])

    return N,M,start,end,graph

while True:
    N,M,start,end,graph = Input()
    dis = Dijkstra(graph,start)
    print(dis)