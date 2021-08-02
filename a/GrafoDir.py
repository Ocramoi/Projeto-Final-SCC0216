#!/usr/bin/env python3

import math
from queue import PriorityQueue


class Grafo:
    nVerts = -1
    adjMatrix = [[]]

    cores = {
        "BRANCO": 0,
        "CINZA": 1,
        "PRETO": 2
    }

    def __init__(self, path: str):
        """
        Inicializa grafo com base no arquivo em [path]
        """
        # Abre arquivo pajek
        with open(path, "r") as arq:
            # Lê linhas
            linhas = arq.readlines()
            # Lê número de vértices do cabeçalho e
            # inicializa matriz de adjacência
            self.nVerts = int(linhas[0].split()[1])
            self.adjMatrix = [([math.inf] * self.nVerts)
                              for _ in range(self.nVerts)]
            # Popula diagonal
            for i in range(self.nVerts):
                self.adjMatrix[i][i] = 0
            # Popula matriz de adjacência a partir do arquivo
            for i in range(2, len(linhas)):
                # Confere formatação da linha
                if len(linhas[i].split()) != 2:
                    continue
                j, k = [int(val) for val in linhas[i].split()[:2]]
                self.adjMatrix[j - 1][k - 1] = 1

    def exibeGrafo(self):
        """
        Exibe matriz de adjacência do grafo formatada
        """
        N = self.nVerts  # Tamanho do lado da matriz
        lenMax = math.ceil(math.log10(N))
        # Exibe rótulos de x
        print("\033[1m",
              "X" * lenMax,
              "|",
              " | ".join([("{:0" + str(lenMax) + "d}").format(x + 1)
                          for x in range(N)]), "\033[0m")
        # Exibe rótulos e valores de cada linha em y
        for linhaN in range(N):
            print("\033[1m",
                  "".join(["-"] * ((lenMax + 3)*(N + 1) - 2)),
                  "\033[0m")
            print(('\033[1m {:0' +
                   str(lenMax) +
                   'd} | \033[0m').format(linhaN + 1),
                  end="")
            print("\033[1m | \033[0m".join([("{:0" +
                                             str(lenMax) +
                                             "d}").format(x)
                                            for x in self.adjMatrix[linhaN]]))

    def dfs(self, vInicio: int, vFim: int) -> int:
        """
        Distância na busca em profundidade a partir de [vInicio] até [vFim]
        """
        # Inicializa vetor auxiliar de distâncias
        dists = [-1] * len(self.adjMatrix)
        return self._dfs(vInicio - 1, 0, dists, vFim - 1)

    def _dfs(self, atual: int, anterior: int,
             dists: [int], destino: int) -> int:
        """
        Implementação 'privada' da busca por profundidade recursiva
        """
        # Marca vértice atual
        dists[atual] = dists[anterior] + 1
        # Confere chegada
        if atual == destino:
            return dists[atual]
        # Procedimento de busca no vértice atual
        for adj in range(self.nVerts):
            if not self.adjMatrix[atual][adj]:
                continue
            if dists[adj] == -1:
                ret = self._dfs(adj, atual, dists, destino)
                if ret != -1:
                    return ret
        return -1

    def detectaCiclo(self, vInicio: int) -> bool:
        """
        Retorna ("cor", "tempoDescoberta", "tempoFinal", "antecessor")
        para cada vértice do grafo referente a pesquisa em profundidade
        a partir de [vInicio] ([1, ...])
        """
        # Inicializa vetor de valores para cada vértice
        valores = [self.cores["BRANCO"] for _ in range(self.nVerts)]
        # Inicia busca recursiva e retorna valores de vértices
        return self._detectaCiclo(vInicio - 1, valores)[0]

    def _detectaCiclo(self,
                      atual: int,
                      valores: [int]) -> [bool, [int]]:
        """
        Implementação 'privada' da busca por profundidade recursiva
        """
        # Atualiza cor para vértice descoberto
        valores[atual] = self.cores["CINZA"]
        # Para todos os vértices
        for adj in range(self.nVerts):
            estat = [val for val in valores]
            # Garante aresta entre o atual
            if not self.adjMatrix[atual][adj]:
                continue
            # Caso vértice não descoberto
            if valores[adj] == self.cores["BRANCO"]:
                # Atualiza tempo e valores chamando recursivamente
                # no vértice descoberto
                ret = self._detectaCiclo(adj, estat)[0]
                if ret:
                    return [True, valores]
            else:
                return [True, valores]

        valores[atual] = self.cores["PRETO"]
        # Retorna tempo e valores dos vértices
        return [False, valores]

    def dijkstra(self, vInicio: int) -> [[int]]:
        """
        Algoritmo de Djikstra para vetorização das distância com
        início em [vInicio]
        """
        # Inicializa valores de vértices
        valores = [
            {
                "distancia": math.inf,
                "antecessor": -1
            }
            for _ in range(self.nVerts)
        ]
        valores[vInicio]['distancia'] = 0

        # Inicia contagem de visitados
        S = [vInicio]

        # Inicializa fila de prioridade de vértices pela sua distância atual
        # (infinito para todos no início, menos vértice inicial)
        Q = PriorityQueue()
        for d in range(self.nVerts):
            Q.put((valores[d]['distancia'], d))

        # Enquanto houver elementos na lista
        while Q.qsize() != 0:
            # Retorna primeiro valor da lista
            u = Q.get()[1]

            # Adiciona atual aos visitados
            S.append(u)

            # entre vértices do grafo
            for adj in range(self.nVerts):
                # Confere adjacência
                if self.adjMatrix[u][adj] == math.inf:
                    continue
                # Caso adjacente, realiza relaxamento se possível
                if valores[adj]['distancia'] > valores[u]['distancia'] + self.adjMatrix[u][adj]:
                    valores[adj]['distancia'] = valores[u]['distancia'] + self.adjMatrix[u][adj]
                    valores[adj]['anterior'] = u

            # Atualiza fila de prioridade
            Q = PriorityQueue()
            for v in range(self.nVerts):
                if v not in S:
                    Q.put((valores[v]['distancia'], v))

        # Retorna vetor de distância
        return [v['distancia'] for v in valores]
