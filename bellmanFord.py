import math
from getCaminho import caminho


def bellmanFord(graph, s, destino):
    dist = []
    pred = []
    Q = []
    i = 0
    j = 0

    # Inicializa dist com infinito e prev com null ou None, pois conhecemos 0 caminhos
    for v in graph:
        dist.append(math.inf)
        pred.append(None)
        Q.append(i) # lista de vértices processados
        i += 1

    dist[s] = 0
    i = 0
    b = 0

    print("Algoritmo de Bellman-Ford")
    print("Origem: ", s)
    print("Destino: ", destino)
    print("Processando...")

    while b <= len(graph):
        trocou = False
        i = 0
        for q in Q:
            j = 1
            for u in graph[i]:
                # Examinamos cada aresta
                adjacente = u[0]
                # caso tenha melhor caminho atualizamos dist e prev
                if dist[adjacente] > dist[i] + u[1]:
                    dist[adjacente] = dist[i] + u[1]
                    pred[adjacente] = i
                trocou = True
                # Caso tenha atualização continuo execução, se n n preciso verificar arestas novamente
                j += 1
            i += 1
        b += 1

        if trocou == False:
            break

    return caminho(pred, s, destino), dist[destino]
