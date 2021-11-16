import math


def floydWarshall(grafo, s, destino):
    i = 0
    j = 0
    k = 0
    dist = []
    pred = []

    while i < len(grafo):
        j = 0
        dist.append([])
        pred.append([])
        while j < len(grafo):
            if i == j:
                dist[i].append(0)
            else:
                dist[i].append(math.inf)
            pred[i].append(None)
            j += 1
        i += 1

    print("Algoritmo de Floyd-Warshall")
    print("Origem: 0")
    print("Destino: ", destino)
    print("Processando...")

    i = 0
    for vert in grafo:
        for aresta in vert:
            dist[i][aresta[0]] = aresta[1]
            pred[i][aresta[0]] = i
        i += 1

    while k < len(grafo):
        i = 0
        while i < len(grafo):
            j = 0
            while j < len(grafo):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
                j += 1
            i += 1
        k += 1

    return dist
