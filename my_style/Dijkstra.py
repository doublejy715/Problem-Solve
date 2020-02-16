import heapq

def Dijkstra(graph,start_node):
    distance = {index : float('inf') for index in graph}
    distance[start_node] = 0
    queue = []
    heapq.heappush(queue,[distance[start_node],start_node])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distance[current_node]:
            continue

        for next_node, next_distance in graph[current_node].items():
            if (distance[current_node] + next_distance) < distance[next_node]:
                distance[next_node] = next_distance + distance[current_node]
                heapq.heappush(queue,[distance[next_node],next_node])

    return distance

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(Dijkstra(mygraph,'A'))
"""import heapq

def Dijkstra(graph,start_node):
    distance = { node : float('inf') for node in graph}
    distance[start_node] = 0
    queue = []
    # distance[start_node] 이때까지 찾은 A-> 해당 노드까지의 최단거리
    heapq.heappush(queue,[distance[start_node],start_node])

    while queue:
        # 현재 그래프까지 오고, 비교한다. -> 먼저 기존의 거리와 팝된 거리를 비교한다.(1차) -> 다음으로 갈 거리까지 비교하고, 거리가 더 낮으면 갈 필요가 있다.
        current_distance, current_node = heapq.heappop(queue)

        # current_distance : current_node 까지 도달하는데 필요한 간선의 weight(경로는 모른다)
        # distance[current_node] : 이때까지 관찰한 current_node까지의 거리
        # ex) distance[current_node] A -> C -> D -> E / current_distance A -> D -> E 의 두 가지 경우
        # 어떻게 도달했는지는 잘 모르겠지만, current_node 까지 오는데 걸린 weight(current_distance)와 현재 가장 짧은 거리의 값과 비교
        if distance[current_node] < current_distance:
            continue

        # 만약에 current_distance가 더 짧다면, 해당 노드를 입력하고 다음 행보를 정한다.
        # 이때까지 온 길이에다가 다음 노드의 경로를 정해준다.
        for next_node, weight in graph[current_node].items():
            # 현재까지 발견된 길이보다 현재 노드에서 다음 노드까지의 길이를 더한것보다 weight가 더 나가게 되면,
            # distance[current_node] == current_distance
            if distance[next_node] > (distance[current_node] + weight):
                distance[next_node] = distance[current_node] + weight
                # 다음 행보가 새롭게 갱신된 경우에만, queue로 넣어준다.
                heapq.heappush(queue,[distance[next_node],next_node])

    return distance
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(Dijkstra(mygraph,'A'))"""