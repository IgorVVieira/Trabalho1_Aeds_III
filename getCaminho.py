def caminho(pred, s, destino):
    caminho = []

    while destino and destino != s:
        caminho.append(destino)
        destino = pred[destino]

    caminho.append(s)
    caminho.reverse()
    return caminho
