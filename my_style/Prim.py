from collections import defaultdict
from heapq import *

def Prim(graph, start_node):
    record = list()
    adjacant_edges = defaultdict(list)
    for weight,n1,n2 in graph:
        adjacant_edges[n1].append([weight,n1,n2])
        adjacant_edges[n2].append([weight,n1,n2])

    connected_node = set(start_node)
    candidate_edges_list = adjacant_edges[start_node]
    heapify(candidate_edges_list)

    while candidate_edges_list:
        weight, node_1, node_2 = heappop(candidate_edges_list)
        if node_2 not in connected_node:
            connected_node.add(node_2)
            record.append([weight,node_1,node_2])

            for edge in adjacant_edges[node_2]:
                if edge[2] not in connected_node:
                    heappush(candidate_edges_list, edge)

    return record
myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]
print(Prim(myedges,'A'))