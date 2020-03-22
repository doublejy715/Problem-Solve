def Cal(mid):
    count = 0
    for index in range(N):
        if request[index] > mid:
            count += mid
        elif request[index] <= mid:
            count += request[index]
    return count

N = int(input())
request = list(map(int,input().split()))
bank = int(input())

start, end = 1, max(request)
while start <= end:
    mid = (start + end) // 2

    # 예산액 보다 많을 시
    if Cal(mid) >= bank:
        end = mid - 1
    else:
        start = mid + 1
print(end)