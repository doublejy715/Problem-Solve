def Find(node):
    if parents[node] != node:
        parents[node] = Find(parents[node])
    return parents[node]

def Union(n1,n2):
    p1,p2 = Find(n1), Find(n2)

    if level[p1] > level[p2]:
        parents[p2] = p1
    elif level[p1] < level[p2]:
        parents[p1] = p2
    else:
        level[p2] += 1
        parents[p1] = p2

def First_Set(graph):
    for node in graph['vertices']:
        parents[node] = node
        level[node] = 0

def Kruskal(graph):
    record = list()
    First_Set(graph)

    edges = graph['edges']
    edges.sort()

    for weight,node_1,node_2 in edges:
        if Find(node_1) != Find(node_2):
            Union(node_1,node_2)
            record.append([weight,node_1,node_2])

    return record







# 간선과 노드의 표현
mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parents = dict()
level = dict()
print(Kruskal(mygraph))