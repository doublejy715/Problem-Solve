import heapq

heap = list()
N, M = map(int,input().split(' '))
data = [0 for i in range(N+1)]
result = list()
for _ in range(M):
    first, second = map(int,input().split(' '))
    data[first] = second

for i in range(1,N+1):
    if i in data:
        continue
    else:
        heapq.heappush(heap,i)


while heap:
    out = heapq.heappop(heap)
    if data[out] != 0:
        heapq.heappush(heap,data[out])
    if out in result:
        continue
    else:
        result.append(out)

for i in result:
    print(i,end=' ')

