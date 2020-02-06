import heapq

N, M = map(int,input().split(' '))
data = list(map(int,input().split(' ')))
plus = list()
minus = list()
largest = max(max(data), - min(data))
for _ in data:
    if _ > 0:
        heapq.heappush(plus,-_)
    else:
        heapq.heappush(minus, _)

result = 0
while plus:
    result += heapq.heappop(plus)
    print(result)
    for index1 in range(M-1):
        if plus:
            heapq.heappop(plus)

while minus:
    result += heapq.heappop(minus)
    for index2 in range(M-1):
        if minus:
            heapq.heappop(minus)

print(-result*2-largest)
