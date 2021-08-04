#!/usr/bin/env python3

# Feito por Marco Antônio Ribeiro de Toledo, RA: 11796419 e Lourenço de Salles Roselino, RA: 11796805

from GrafoDir import Grafo
import math


def main():
    # Lê nome do arquivo a ser analisado
    arquivo = input()
    # Cria grafo com base noa rquivo
    grafo = Grafo(arquivo)

    # Inicializa número de sorvedouros
    numSorvedouros = 0
    # Para cada vértice
    for linha in grafo.adjMatrix:
        # Confere se vértice é pai de outro
        flag = True
        for i in linha:
            if i not in [math.inf, 0]:
                flag = False
                break
        # Caso não possua filho, contabiliza
        if flag:
            numSorvedouros += 1

    # Exibe número de sorvedouros contabilizado
    print(numSorvedouros)


if __name__ == "__main__":
    main()
