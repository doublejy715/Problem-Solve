from collections import deque

# 이진 탐색을 위해서 정해주어야 하는 것, 어떤 것을 탐색할지, max min을 어떻게 정할지,

n, m = map(int,input().split())
adj = [[] for _ in range(n+1)]

start = 10000000000
end = 1

def Bfs(c):
    queue = deque([start_node])
    visited = [False] * (n+1)
    visited[start_node] = True

    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight <= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]


for _ in range(m):
    a, b, weight = map(int,input().split())
    adj[a].append((b,weight))
    adj[b].append((a,weight))
    start = min(weight,start)
    end = max(weight,end)

start_node, end_node = map(int,input().split())

result = start
while start <= end :
    mid = (start + end) // 2
    if Bfs(mid):
        result = mid
        start += 1
    else:
        end = mid-1
print(result)