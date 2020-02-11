# 컴퓨터의 수가 적으므로 DFS를 이용하는것이 유리하다 한다.(여기서는 100개)

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]

visited = [False] * (n+1)
count = 0
for _ in range(m):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

def dfs(now_pos): # 시작하는 부분 여기서는 1이 될듯
    global count
    count += 1
    visited[now_pos] = True
    for nex_pos in adj[now_pos]:
        if not visited[nex_pos]:
            dfs(nex_pos)

dfs(1)
print(count-1)
