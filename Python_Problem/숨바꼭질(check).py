from collections import deque

MAX = 100001
n, k = map(int,input().split())
array = [0] * MAX

def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k: # 시작위치와 도착위치가 일치하면 0으로 마무리, (보통 여기에 문제적 조건을 단다)
            return array[now_pos]
        # 출발위치와 도착위치가 다른경우
        for nex_pos in (now_pos-1, now_pos+1, now_pos*2):
            if 0 <= nex_pos < MAX and not array[nex_pos]: # 범위를 벗어나지 않고, 방문한적도 없다면,
                array[nex_pos] = array[now_pos] + 1 # 기존의 시간에다가 1을 더해서 다음으로 넘긴다.
                q.append(nex_pos)

print(bfs())