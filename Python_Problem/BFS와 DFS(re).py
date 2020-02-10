from collections import deque

# 스택 대신 재귀함수의 이용
# 원래 스택을 이용해서 할 수 있으나 재귀함수를 이용해서도 할 수 있다.
def dfs(v):
    print(v,end=' ')
    visited[v] = True # 방문한 곳을 표시해 준다.
    for e in adj[v]: # 방문한 노드와 인접한 인자들을 한번씩 넣어보면서(이미 정렬되었으므로 낮은 순으로 간다.)
        if not(visited[e]): # 인자의 값이 True가 아니면, dfs를 호출한다.
            dfs(e) # dfs를 부르면 해당 인자로 넘어가는 의미이다.

# 큐를 필요로 하므로 deque를 이용
def bfs(v):
    # 시작 노드점을 정해준다.
    q = deque([v]) # 이 모습이 deque형식의 list를 지정하는 방법이다. [v] 가 deque형식으로 만들어 진다.
    while q: # 큐가 빌때까지 지속한다.
        v = q.popleft() # q 내부의 원소를 꺼낸다.(노드를 방문한다.)
        if not (visited[v]): # 방문한 적이 없다면,(검사)
            visited[v] = True # 방문한 것으로 mark
            print(v, end=' ')
            for e in adj[v]: # 방문한 노드와 인접한 노드들의 값을 꺼내온다. 만약 방문한적이 없다면,
                if not visited[e]:
                    q.append(e) # q에 원소(노드를) 추가한다.


n, m, v = map(int,input().split(' '))
adj = [[]for _ in range(n+1)] # 정점마다의 정보를 담아두기 위해서 n+1개 만든다.

for _ in range(m):
    # 각 노드들이 어디에 연결되어 있는지 정보를 저장한다.
    x,y = (map(int,input().split(' ')))
    adj[x].append(y)

# 각 노드들의 원소들을 정렬하여준다.
for e in adj:
    e.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
