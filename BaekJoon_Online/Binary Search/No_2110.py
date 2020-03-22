import sys
read = sys.stdin.readline

N,C = map(int,read().split())
point = [int(read().strip()) for _ in range(N)]
point.sort()
start, end = 1,point[-1]-point[0]
result = 0
def Install(distance):
    count = 1
    cur_point = point[0]
    for index in range(1,N):
        if point[index] - cur_point >= distance:
            count += 1
            cur_point = point[index]
    return count


while start <= end:

    mid = (start+end) // 2

    # 공유기 설지하는 것이 필요한 갯수보다 더 적을때 -> 간선을 줄인다.
    if Install(mid) < C:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
