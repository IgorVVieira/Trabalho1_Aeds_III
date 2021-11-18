import math
from getCaminho import caminho


def dijkstra(grafo, s, destino):
    dist = []
    pred = []
    Q = []
    i = 0
    excluidos = []
    aux = grafo

    for v in grafo:
        dist.append(math.inf)
        pred.append(None)
        Q.append(i)
        i += 1

    dist[s] = 0
    print("Algoritmo de Dijkstra")
    print("Origem: ", s)
    print("Destino: ", destino)
    print("Processando...")

    for q in Q:
        menor, u = buscaMenor(dist, excluidos)
        excluidos.append(u)
        i = 0

        for v in aux[u]:
            if dist[v[0]] > dist[u] + v[1]:
                dist[v[0]] = dist[u] + v[1]
                pred[v[0]] = u
            i += 1

    custo = dist[destino]

    return caminho(pred, s, destino), custo


def buscaMenor(lista, excluidos):
    menor = math.inf
    pos = 0
    i = 0

    while i < len(lista):
        if i in excluidos:
            i += 1
            continue
        if lista[i] < menor:
            menor = lista[i]
            pos = i
        i += 1

    return menor, pos
