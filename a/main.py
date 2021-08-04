#!/usr/bin/env python3

# Feito por Marco Antônio Ribeiro de Toledo, RA: 11796419 e Lourenço de Salles Roselino, RA: 11796805

from GrafoDir import Grafo
import math


def main():
    # Lê nome do arquivo a ser analisado
    arquivo = input()
    # Cria grafo com base noa rquivo
    grafo = Grafo(arquivo)

    # Inicializa número de fontes
    numFontes = 0
    # Para cada vértice
    for i in range(grafo.nVerts):
        # Confere se outro vértice é pai do analisado
        flag = True
        for j in range(grafo.nVerts):
            if grafo.adjMatrix[j][i] not in [math.inf, 0]:
                flag = False
                break
        # Caso não possua pai, contabiliza
        if flag:
            numFontes += 1

    # Exibe número de fontes contabilizado
    print(numFontes)


if __name__ == "__main__":
    main()
