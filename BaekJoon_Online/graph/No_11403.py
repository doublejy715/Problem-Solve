def Input(nodes):
    for i in range(N):
        data = list(map(int, input().split()))
        tmp = []
        # 이어진 부분 노드 기록해주기
        for j in range(len(data)):
            if data[j] == 1:
                tmp.append(j)
        nodes[i] = tmp
    return nodes

def Dfs(nodes,graph):
    for i in range(len(nodes)):
        need_visit, visited = [], []
        need_visit.append(i)
        count = 0             # 처음 시작지점 건너뛰기 위함
        while need_visit:
            node = need_visit.pop()
            if node not in visited:
                need_visit.extend(nodes[node])
                if count != 0:
                    graph[i][node] = 1
                    visited.append(node)
            count += 1

def Output(graph):
    for i in range(len(graph)):
        print(*graph[i], sep=' ')

N = int(input())
nodes = dict()
nodes = Input(nodes)
graph = [[0 for _ in range(N)] for _ in range(N)]
Dfs(nodes,graph)
Output(graph)

