import heapq

N = int(input())
heap = list()
result = list()
for index in range(N):
    num = int(input())
    if len(heap) == 0 and num == 0:
        result.append(0)
    elif num == 0:
        result.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap,num)

for index1 in result:
    print(index1)