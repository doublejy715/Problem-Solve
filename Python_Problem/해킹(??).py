from collections import defaultdict
import heapq

def Search(graph,start):
    adj = {_ : float('inf') for _ in graph}
    adj[start] = 0
    count = 0
    queue = list()
    heapq.heappush(queue,[adj[start],start])
    while queue:
        current_weight, current_com = heapq.heappop(queue)
        if current_weight > adj[current_com]:
            continue
        for next_weight,next_com in graph[current_com]:
            if current_weight + next_weight < adj[next_com]:
                adj[next_com] = adj[current_com] + next_weight
                heapq.heappush(queue,[adj[next_com],next_com])
                count += 1

    return adj, count


test_case = int(input())
for _ in range(test_case):
    n,d,c = map(int,input().split())

    graph = defaultdict(list)

    for index in range(d):
        a, b, s = map(int,input().split())
        graph[b].append((s,a))
        graph[a].append((s,b))

    adj1, count1 = Search(graph,c)
    print(count1, max(adj1.values()))