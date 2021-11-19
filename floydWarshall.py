import math
from getCaminho import caminho


def floydWarshall(graph, s, destino):
    i, j, k = 0, 0, 0
    dist = []
    pred = []

    while i < len(graph):
        j = 0
        dist.append([])
        pred.append([])
        while j < len(graph):
            if i == j:
                dist[i].append(0)
            else:
                dist[i].append(math.inf)
            pred[i].append(None)
            j += 1
        i += 1

    print("Algoritmo de Floyd-Warshall")
    print("Origem: ", s)
    print("Destino: ", destino)
    print("Processando...")

    i = 0
    for vert in graph:
        for aresta in vert:
            dist[i][aresta[0]] = aresta[1]
            pred[i][aresta[0]] = i
        i += 1

    while k < len(graph):
        i = 0
        while i < len(graph):
            j = 0
            while j < len(graph):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
                j += 1
            i += 1
        k += 1

    return 0, dist
