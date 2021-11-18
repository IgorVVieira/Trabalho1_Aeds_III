import timeit
from dijkstra import dijkstra
from bellmanFord import bellmanFord
from floydWarshall import floydWarshall


def main():
    try:
        file = input('Informe o arquivo: ')
        # ./Datasets/toy.txt
        origem = int(input('Origem: '))
        destino = int(input('Destino: '))

        algoritmo = int(
            input('Algoritmo:\n \t1 Dijkstra \n \t2 Bellman-Ford \n \t3 Floyd-Warshal\n'))
        lerArquivo(file, origem, destino, algoritmo)
    except:
        print('Por favor, insira um número inteiro. Tente novamente!')


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
                inicio = timeit.default_timer()
                caminho, custo = dijkstra(G, origem, destino)

                fim = timeit.default_timer()
                print('Custo:', custo)
                print('Caminho: ', caminho)
                print('Tempo: %.3f s' % (fim - inicio))
            elif algoritmo == 2:
                inicio = timeit.default_timer()
                caminho, custo = bellmanFord(G, origem, destino)

                fim = timeit.default_timer()
                print('Custo:', custo)
                print('Caminho: ', caminho)
                print('Tempo: %.3f s' % (fim - inicio))
            elif algoritmo == 3:
                inicio = timeit.default_timer()

                caminho, custo = floydWarshall(G, origem, destino)
                fim = timeit.default_timer()
                print('Custo:', custo)
                print('Caminho: ', caminho)
                print('Tempo: %.3f s' % (fim - inicio))
            else:
                print('Algoritmo inválido selecionado, tente novamente!')
                quit()  # Finaliza execução caso não encontre o algoritmo
            f.close()
        return
    except:
        print('Não foi posível ler o arquivo, tente novamente.')


main()
