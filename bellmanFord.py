import math
from getCaminho import caminho


def bellmanFord(grafo, s, destino):
    dist = []
    pred = []
    Q = []
    i = 0
    j = 0

    for v in grafo:
        dist.append(math.inf)
        pred.append(None)
        Q.append(i)
        i += 1

    dist[s] = 0
    i = 0
    b = 0

    print("Algoritmo de Bellman-Ford")
    print("Origem: ", s)
    print("Destino: ", destino)
    print("Processando...")

    while b <= len(grafo):
        trocou = False
        i = 0
        for q in Q:
            j = 1

            for u in grafo[i]:
                adjacente = u[0]
                if dist[adjacente] > dist[i] + u[1]:
                    dist[adjacente] = dist[i] + u[1]
                    pred[adjacente] = i
                trocou = True
                j += 1
            i += 1
        b += 1

        if trocou == False:
            break

    return caminho(pred, s, destino), dist[destino]
