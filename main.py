import dijkstra
import bellmanFord
import floydWarshall


def main():
    try:
        file = input('Informe o arquivo: ')
        # ./Datasets/toy.txt
        origem = int(input('Origem: '))
        destino = int(input('Destino: '))

        algoritmo = int(
            input('Algoritmo:\n \t1 Dijkstra \n \t2 Bellman-Ford \n \t3- Floyd-Warshal\n'))
        lerArquivo(file, origem, destino, algoritmo)
    except:
        print('Por favor, insira um número inteiro. Tente novamente!')

    # aux = grafo[s:destino]


def lerArquivo(file, origem, destino, algoritmo):
    try:
        with open(file, "r") as f:
            header = f.readline().split()
            G = [[] for _ in range(int(header[0]))]  # Tamanho do grafo

            for line in f:
                if len(line.split()) == 2:  # Pula a primeira linha contendo cabeçalho
                    continue
                valores = (*map(int, line.split()), )
                G[valores[0]].append(valores[1:])

            if algoritmo == 1:
                print(dijkstra.dijkstra(G, origem, destino))
            elif algoritmo == 2:
                print(bellmanFord.bellmanFord(G, origem, destino))
            elif algoritmo == 3:
                print(floydWarshall.floydWarshall(G, origem, destino))
            else:
                print('Algoritmo inválido selecionado, tente novamente!')
            f.close()
    except:
        print('Não foi posível ler o arquivo, tente novamente.')


main()
