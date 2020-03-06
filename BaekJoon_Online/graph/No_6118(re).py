import heapq

N, M = map(int,input().split())
data = []
# 데이터 정렬
for _ in range(M):
    x,y = map(int,input().split())
    if x > y:
        x, y = y, x
    data.append([x,y])

# 다익스트라 구현
dis = { _ : float('inf') for _ in range(N+1)}
dis[0],dis[1] = 0,0
queue = []
heapq.heappush(queue,1)

while queue:
    node = heapq.heappop(queue)
    for A_i,B_i in data:
        if A_i == node:
            if B_i not in queue:
                heapq.heappush(queue,B_i)
            if dis[B_i] > dis[A_i] + 1:
                dis[B_i] = dis[A_i] + 1

# 출력 조절
count = 0
lists = []
for j in range(M):
    if max(dis.values()) == dis[j]:
        lists.append(j)
        count += 1

print(min(lists),max(dis.values()),count)