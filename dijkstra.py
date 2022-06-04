import networkx as nx
import matplotlib.pyplot as plt
import sys
import random
from heapq import heapify, heappush, heappop

def creatGraph(nodes, shortestPath):
    G = nx.Graph()
    plt.figure()
    edges = []
    n = len(nodes)
    for i in range(n):
        if nodes[i] in shortestPath:

            G.add_node(nodes[i], nodetype="red")
        if nodes[i] not in shortestPath:
            G.add_node(nodes[i], nodetype="blue")


    G.add_edges_from([(nodes[0], nodes[1]), (nodes[0], nodes[2]), (nodes[1], nodes[2]), (nodes[1], nodes[3]),
                      (nodes[1], nodes[0]), (nodes[2], nodes[0]),
                      (nodes[2], nodes[1]), (nodes[2], nodes[3]),
                      (nodes[3], nodes[1]), (nodes[3], nodes[2]),
                      (nodes[3], nodes[4]), (nodes[4], nodes[2]),
                      (nodes[4], nodes[3]), (nodes[4], nodes[5]),
                      (nodes[5], nodes[3]), (nodes[5], nodes[4])])

    colors = [u[1] for u in G.nodes(data="nodetype")]
    pos = nx.spring_layout(G)
    nx.draw(G, pos,  with_labels=True, node_color=colors)

    nx.draw_networkx_edge_labels(G, pos,  edge_labels={(nodes[0], nodes[1]): 10,
                                                       (nodes[0], nodes[2]): edgeData['A-C']['cost'],
                                                       (nodes[1], nodes[2]): edgeData['B-C']['cost'],
                                                       (nodes[1], nodes[3]): edgeData['B-D']['cost'],
                                                       (nodes[1], nodes[0]): edgeData['B-A']['cost'],
                                                       (nodes[2], nodes[0]): edgeData['C-A']['cost'],
                                                       (nodes[2], nodes[1]): edgeData['C-B']['cost'],
                                                       (nodes[2], nodes[3]): edgeData['C-D']['cost'],
                                                       (nodes[3], nodes[1]): edgeData['D-B']['cost'],
                                                       (nodes[3], nodes[2]): edgeData['D-C']['cost'],
                                                       (nodes[3], nodes[4]): edgeData['D-E']['cost'],
                                                       (nodes[4], nodes[2]): edgeData['E-C']['cost'],
                                                       (nodes[4], nodes[3]): edgeData['E-D']['cost'],
                                                       (nodes[4], nodes[5]): edgeData['E-F']['cost'],
                                                       (nodes[5], nodes[3]): edgeData['F-D']['cost'],
                                                       (nodes[5], nodes[4]): edgeData['F-E']['cost']
                                                       })
    plt.show()

def dijkstra(graph, src, dest):
    inf = sys.maxsize
    nodeData = {'A': {'cost': inf, 'pred': []},
                 'B': {'cost': inf, 'pred': []},
                 'C': {'cost': inf, 'pred': []},
                 'D': {'cost': inf, 'pred': []},
                 'E': {'cost': inf, 'pred': []},
                 'F': {'cost': inf, 'pred': []}}

    edgeData = []

    nodeData[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(5):
        if temp not in visited:
            visited.append(temp)
            minHeap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = nodeData[temp]['cost'] + graph[temp][j]
                    if cost < nodeData[j]['cost']:
                        nodeData[j]['cost'] = cost
                        nodeData[j]['pred'] = nodeData[temp]['pred'] + list(temp)
                    heappush(minHeap, (nodeData[j]['cost'], j))
        heapify(minHeap)
        temp = minHeap[0][1]
    shortestPath = nodeData[dest]['pred'] + list(dest)
    print("el camino mas corto es: " + str(nodeData[dest]['pred'] + list(dest)))
    creatGraph(list(graph.keys()), shortestPath)



graph = {
    'A': {'B': random.randint(1, 20), 'C': random.randint(1, 20)},
    'B': {'A': random.randint(1, 20), 'C': random.randint(1, 20), 'D': random.randint(1, 20)},
    'C': {'A': random.randint(1, 20), 'B': random.randint(1, 20), 'E': random.randint(1, 20), 'D': random.randint(1, 20)},
    'D': {'B': random.randint(1, 20), 'C': random.randint(1, 20), 'E': random.randint(1, 20), 'F': random.randint(1, 20)},
    'E': {'C': random.randint(1, 20), 'D': random.randint(1, 20), 'F': random.randint(1, 20)},
    'F': {'D': random.randint(1, 20), 'E': random.randint(1, 20)}
}

edgeData = {
    'A-B': {'cost': graph['A']['B']},
    'A-C': {'cost': graph['A']['C']},
    'B-A': {'cost': graph['B']['A']},
    'B-C': {'cost': graph['B']['C']},
    'B-D': {'cost': graph['B']['C']},
    'C-A': {'cost': graph['C']['A']},
    'C-B': {'cost': graph['C']['B']},
    'C-E': {'cost': graph['C']['E']},
    'C-D': {'cost': graph['C']['D']},
    'D-B': {'cost': graph['D']['B']},
    'D-C': {'cost': graph['D']['C']},
    'D-E': {'cost': graph['D']['E']},
    'D-F': {'cost': graph['D']['F']},
    'E-C': {'cost': graph['E']['C']},
    'E-D': {'cost': graph['E']['D']},
    'E-F': {'cost': graph['E']['F']},
    'F-D': {'cost': graph['F']['D']},
    'F-E': {'cost': graph['F']['E']}
}

for i in edgeData:
    print(edgeData[i])


source = 'A'
destination = 'F'
dijkstra(graph, source, destination)


