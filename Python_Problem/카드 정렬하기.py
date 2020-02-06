import heapq


N = int(input())
heap = list()
count = 0
result = 0
for i in range(N):
    data = int(input())
    heapq.heappush(heap, data)

while len(heap) != 1:
    data1 = heapq.heappop(heap)
    data2 = heapq.heappop(heap)
    count = data1 + data2
    heapq.heappush(heap, count)
    result += count

print(result)