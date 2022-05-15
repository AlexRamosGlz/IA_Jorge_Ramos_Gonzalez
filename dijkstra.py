import networkx as nx
import matplotlib.pyplot as plt
import sys
import random
from heapq import heapify, heappush, heappop

def creatGraph(nodes, shortestPath):
    G = nx.Graph()

    print(nodes)
    n = len(nodes)
    for i in range(n):
        if nodes[i] in shortestPath:
            print(nodes[i])
            G.add_node(nodes[i], nodetype="red")
        if nodes[i] not in shortestPath:
            G.add_node(nodes[i], nodetype="blue")

    G.add_edges_from([(nodes[0], nodes[1]), (nodes[0], nodes[2]),
                      (nodes[1], nodes[2]), (nodes[1], nodes[3]),
                      (nodes[1], nodes[0]), (nodes[2], nodes[0]),
                      (nodes[2], nodes[1]), (nodes[2], nodes[3]),
                      (nodes[3], nodes[1]), (nodes[3], nodes[2]),
                      (nodes[3], nodes[4]), (nodes[4], nodes[2]),
                      (nodes[4], nodes[3]), (nodes[4], nodes[5]),
                     (nodes[5], nodes[3]), (nodes[5], nodes[4])])
    print(G.nodes().data())
    colors = [u[1] for u in G.nodes(data="nodetype")]
    nx.draw(G, with_labels=True, node_color=colors)
    plt.show()

def dijkstra(graph, src, dest):
    inf = sys.maxsize
    nodeData = {'A': {'cost': inf, 'pred': []},
                 'B': {'cost': inf, 'pred': []},
                 'C': {'cost': inf, 'pred': []},
                 'D': {'cost': inf, 'pred': []},
                 'E': {'cost': inf, 'pred': []},
                 'F': {'cost': inf, 'pred': []}}

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
    creatGraph(list(graph.keys()), shortestPath)
    print("el camino mas corto es: " + str(nodeData[dest]['pred'] + list(dest)))


graph = {
    'A': {'B': random.randint(1, 20), 'C': random.randint(1, 20)},
    'B': {'A': random.randint(1, 20), 'C': random.randint(1, 20), 'D': random.randint(1, 20)},
    'C': {'A': random.randint(1, 20), 'B': random.randint(1, 20), 'E': random.randint(1, 20), 'D': random.randint(1, 20)},
    'D': {'B': random.randint(1, 20), 'C': random.randint(1, 20), 'E': random.randint(1, 20), 'F': random.randint(1, 20)},
    'E': {'C': random.randint(1, 20), 'D': random.randint(1, 20), 'F': random.randint(1, 20)},
    'F': {'D': random.randint(1, 20), 'E': random.randint(1, 20)}
}

source = 'A'
destination = 'F'
dijkstra(graph, source, destination)


