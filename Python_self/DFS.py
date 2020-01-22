
graph = dict()
graph['A'] = ['B','C']
graph['B'] = ['A','D']
graph['C'] = ['A','G','H','I']
graph['D'] = ['B','E','F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C','J']
graph['J'] = ['I']

def DFS(graph,start_node):
    visited, need_visit = list(),list()             # 방문한 곳(큐), 방문할 곳(스텍)을 기록한다.
    need_visit.append(start_node)                      # 시작할 노드부터 넣는다.

    while need_visit:                               # need_visit 내부에 값이 있을 동안에 작동한다.
        node = need_visit.pop()
        if node not in visited:                     # 만약 방문하지 않았다면
            visited.append(node)
            need_visit.extend(graph[node])
    return print(visited)

DFS(graph,'A')
