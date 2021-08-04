#!/usr/bin/env python3

# Feito por Marco Antônio Ribeiro de Toledo, RA: 11796419 e Lourenço de Salles Roselino, RA: 11796805

from GrafoDir import Grafo
import math


# Retorna os pais de um vertice
def confereDfs(vert: int, grafo: Grafo) -> [int]:
    # Lista de pais do vértice
    pais = []

    # Procura pais
    for i in range(grafo.nVerts):
        if grafo.adjMatrix[i][vert] == 1:
            pais.append(i)

    # Confere se nenhum dos pais é disconexo ao vértice 1
    for pai in pais:
        if grafo.dfs(1, pai + 1) == -1:
            return []


    return pais 


def main():
    # Lê nome do arquivo a ser analisado
    arquivo = input()
    # Cria grafo com base noa rquivo
    grafo = Grafo(arquivo)
    # Encontra as distancias do grafo usando um dijkstra
    distancias = grafo.dijkstra(0)
    # Pais das folhas
    dictPais = {}
    distanciasFolhas = grafo.nVerts * [math.inf]

    # Para cada vértice
    for linha in range(grafo.nVerts):
        # Confere se vértice é pai de outro
        flag = True
        for i in grafo.adjMatrix[linha]:
            if i not in [math.inf, 0]:
                flag = False
                break
        # Caso não possua filho (é sorvedouro), contabiliza
        if flag:
            pais = confereDfs(linha, grafo)
            if len(pais) != 0:
                dictPais[linha] = pais
                distanciasFolhas[linha] = distancias[pais[0]] + distancias[pais[1]]
    valorMinimo = min(distanciasFolhas)
    for i in range(grafo.nVerts):
        if distanciasFolhas[i] <= valorMinimo:
            print(i+1)


if __name__ == "__main__":
    main()
