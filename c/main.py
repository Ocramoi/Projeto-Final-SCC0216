#!/usr/bin/env python3

from GrafoDir import Grafo
import math


# Realiza busca em profundidade no [grafo] do vértice 1 a [vert]
def confereDfs(vert: int, grafo: Grafo) -> bool:
    # Lista de pais do vértice
    pais = []

    # Procura pais
    for i in range(grafo.nVerts):
        if grafo.adjMatrix[i][vert] == 1:
            pais.append(i)

    # Confere se nenhum dos pais é disconexo ao vértice 1
    for pai in pais:
        if grafo.dfs(1, pai + 1) == -1:
            return False

    # Exibe vértice dado
    print(vert + 1)

    return True


def main():
    # Lê nome do arquivo a ser analisado
    arquivo = input()
    # Cria grafo com base noa rquivo
    grafo = Grafo(arquivo)

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
            confereDfs(linha, grafo)


if __name__ == "__main__":
    main()
