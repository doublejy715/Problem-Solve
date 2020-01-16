def BFS(graph,start_node):
    # 먼저 visited list 와 need_visit list 를 형성한다.
    visited, need_visit = list(),list()

    # 다음으로 시작 노드부터 need_visit 에 넣어준다.
    need_visit.append(start_node)
    count = 0  # 이건 단순히 몇개의 노드가 존재하는지 알려주기 위한 척도
    while need_visit:  # 더이상 방문할 노드가 없을때까지 반복한다.
        node = need_visit.pop(0)  # 먼저 이번턴에서 방문할 노드를 꺼낸다.
        if node not in visited:  # 만약 visited list 에 node 가 없으면 넣어준다.
            visited.append(node)
        # 들어오는 graph 형태는 dict 형식으로 들어온다. node 를 이용하여 불러올 dict 을 명시한다.
            need_visit.extend(graph[node])  # 추가적으로 확장시켜줄 때 extend 를 이용한다.
        count += 1
    print(count)
    return visited


graph1 = dict() # dict 이건 뭐지?
# A 카테고리 안에 B, C 의 원소가 존재한다. 원소는 list형태로 저장된다.
graph1['A'] = ['B', 'C']
graph1['B'] = ['A', 'D']
graph1['C'] = ['A', 'G', 'H', 'I']
graph1['D'] = ['B', 'E', 'F']
graph1['E'] = ['D']
graph1['F'] = ['D']
graph1['G'] = ['C']
graph1['H'] = ['C']
graph1['I'] = ['C', 'J']
graph1['J'] = ['I']
print(BFS(graph1, 'A'))

