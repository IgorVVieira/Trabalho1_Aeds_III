import math
from getCaminho import caminho


def dijkstra(graph, s, destino):
    dist = []
    pred = []
    Q = []
    i = 0
    excluidos = []  # vertices n processados
    graphAux = graph

    # Inicializa dist com infinito e prev com null ou None, pois conhecemos 0 caminhos
    for v in graph:
        dist.append(math.inf)
        pred.append(None)
        Q.append(i)  # lista de vértices processados
        i += 1

    dist[s] = 0
    print("Algoritmo de Dijkstra")
    print("Origem: ", s)
    print("Destino: ", destino)
    print("Processando...")

    for q in Q:
        # Busco menor distância dentre os elementos de Q
        u = getMenor(dist, excluidos)
        excluidos.append(u)
        i = 0

        for v in graphAux[u]:
            if dist[v[0]] > dist[u] + v[1]:
                # Se é vdd tenho um novo melhor caminho a partir de u
                dist[v[0]] = dist[u] + v[1]
                pred[v[0]] = u
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

    return posicao
