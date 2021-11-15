import dijkistra


def main():
    try:
        file = input('Informe o arquivo: ')
        # ./Datasets/toy.txt
        origem = int(input('Origem: '))
        destino = int(input('Destino: '))
        with open(file, "r") as f:
            header = f.readline().split()
            G = [[] for _ in range(int(header[0]))]  # Tamanho do grafo

            for line in f:
                if len(line.split()) == 2:  # Pula a primeira linha contendo cabeçalho
                    continue
                valores = (*map(int, line.split()), )
                G[valores[0]].append(valores[1:])

            print(G)
            print(dijkistra.dijkstra(G, origem, destino))
            f.close()
    except:
        print('Não foi posível ler o arquivo, tente novamente.')


main()
