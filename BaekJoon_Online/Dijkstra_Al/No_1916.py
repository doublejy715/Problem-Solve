import sys,heapq
read = sys.stdin.readline
Inf = sys.maxsize

def Dijkstra(graph,start,end):

    distance = [Inf]*(town+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue,[distance[start],start])

    while queue:
        cur_dis, cur_house = heapq.heappop(queue)

        if distance[cur_house] < cur_dis:
            continue

        for next_house,next_dis in graph[cur_house]:
            if distance[next_house] > next_dis + distance[cur_house]:
                distance[next_house] = next_dis + distance[cur_house]
                heapq.heappush(queue,[distance[next_house],next_house])
    return distance[end]


def Input():
    town = int(read().strip())
    graph = [[] for _ in range(town+1)]
    M = int(read().strip())
    for i in range(M):
        start,end,edge = map(int,read().strip().split())
        graph[start].append([end,edge])

    start,end = map(int,read().strip().split())
    return town,graph,start,end

town,graph,start,end = Input()
print(Dijkstra(graph,start,end))
