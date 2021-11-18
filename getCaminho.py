def caminho(pred, s, destino):
    caminho = []
    destinoAuxiliar = destino

    while destinoAuxiliar and destinoAuxiliar != s:
        caminho.append(destinoAuxiliar)
        destinoAuxiliar = pred[destinoAuxiliar]

    caminho.append(s)
    caminho.reverse()
    return caminho
