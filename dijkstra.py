import math
from getCaminho import caminho


def dijkstra(graph, s, destino):
    dist = []
    pred = []
    Q = []
    i = 0
    excluidos = []
    aux = graph

    for v in graph:
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
        menor, posicao = getMenor(dist, excluidos)
        excluidos.append(posicao)
        i = 0

        for v in aux[posicao]:
            if dist[v[0]] > dist[posicao] + v[1]:
                dist[v[0]] = dist[posicao] + v[1]
                pred[v[0]] = posicao
            i += 1

    return caminho(pred, s, destino), dist[destino]


def getMenor(lista, excluidos):
    menor = math.inf
    posicao = 0
    i = 0

    while i < len(lista):
        if i in excluidos:
            i += 1
            continue
        if lista[i] < menor:
            menor = lista[i]
            posicao = i
        i += 1

    return menor, posicao
